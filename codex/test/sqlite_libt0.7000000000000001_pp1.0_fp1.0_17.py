import ctypes
import ctypes.util
import threading
import sqlite3

# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
# https://docs.python.org/3/library/sqlite3.html
# https://stackoverflow.com/questions/24620492/python-sqlite3-executemany-with-dictionary-argument


def log_request(ip_address, country, city, api_key, api_secret):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    sql_command = """INSERT INTO logs (ip_address, country, city, api_key, api_secret, timestamp) VALUES (?, ?, ?, ?, ?, ?);"""

    cursor.execute(sql_command, (ip_address, country, city, api_key, api_secret, int(time.time())))
    connection.commit()


def log_error(error_type, error_message, api_key, api_secret):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    sql
