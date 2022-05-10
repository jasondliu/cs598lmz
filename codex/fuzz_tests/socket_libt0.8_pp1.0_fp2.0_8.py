import socket
import threading
import sqlite3
from sqlite3 import Error

database = "database.db"

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return None

conn = create_connection(database)
cur = conn.cursor()

def write_query(data):
    try:
        cur.execute('INSERT INTO data (id,date,time,value) VALUES (?,?,?,?)',data)
        conn.commit()
        return True
    except Error as e:
        print(e)
    return False

def read_query(id,date):
    try:
        query = 'SELECT * FROM data WHERE id = {} AND date = {} ORDER BY time ASC'.format(id,date)
        cur.execute(query)
        return cur.fetchall()
    except Error as e:
        print(e)
    return None

def read_tank():
    try:
        cur.execute("SELECT * FROM tank
