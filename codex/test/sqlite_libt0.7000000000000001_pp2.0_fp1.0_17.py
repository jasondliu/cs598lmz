import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import subprocess


def check_file(filename):
    try:
        with open(filename):
            pass
    except IOError:
        return False
    return True

def create_db(filename):
    if check_file(filename) == True:
        print("Database does exist. Continue program.")
    else:
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, time INTEGER, x REAL, y REAL, z REAL);")
        c.execute("CREATE TABLE IF NOT EXISTS info (id INTEGER, value TEXT);")
        c.execute("INSERT INTO info VALUES (0, '0');")
        conn.commit()
        conn.close()

def write_db(filename, x, y, z):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
