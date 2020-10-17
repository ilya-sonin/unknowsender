# Спам бот для телегррамм
Ссылка на бота - @unknown_sender_bot

## Общая инструкция
Клонируем
```
git clone https://github.com/Ilya001/unknowsender
```
Создаем общее виртуальное окружение и устанавливаем все
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
## Запуск бота
Бота мы запускаем с помощью systemctl. Файл unksend_bot.service помещаем в папку /etc/systemd/system вот такой командой:
```
cp home/unknowsender/unknowsender.service /etc/systemd/system
```
Далее общие команды для запуска

systemctl daemon-reload
systemctl enable unksend_bot
systemctl start unksend_bot
systemctl status unksend_bot
