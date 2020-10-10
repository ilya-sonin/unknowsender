# Import modules
import sqlite3 as sql

# Get api token from database
def get_token():
    db_connect = sql.connect("db.sqlite3")
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM telegram_data;")
    token = cur.fetchone()[0]
    return token


# Checking the username for uniqueness and writing
def add_user(username, chat_id):
    db_connect = sql.connect("db.sqlite3")
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM users;")
    users_data = cur.fetchall()
    usernames = [i[1] for i in users_data]
    chat_ids = [i[2] for i in users_data]
    if (username not in usernames) and (chat_id not in chat_ids):
        cur.execute("""INSERT INTO users(username, chat_id) VALUES("{}", {});""".format(username, chat_id))
        db_connect.commit()


# Get chat_ids
def get_users_chat_ids():
    db_connect = sql.connect("db.sqlite3")
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM users;")
    users_data = cur.fetchall() 
    chat_ids = [i[2] for i in users_data]
    return chat_ids
