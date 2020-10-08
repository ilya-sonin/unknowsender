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
def add_user(chat_id):
    db_connect = sql.connect("db.sqlite3")
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM users;")
    users_data = cur.fetchall() 
    chat_ids = [i[1] for i in users_data]
    if chat_id not in chat_ids:
        cur.execute(f"INSERT INTO users(chat_id) VALUES('{chat_id}');")
        db_connect.commit()