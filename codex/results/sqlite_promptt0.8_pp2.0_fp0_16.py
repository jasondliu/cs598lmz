import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# global test

def check_existing_connection(connection):
    conn_lock = threading.Lock()
    conn_lock.acquire()
    # print("Lock Acquired.")
    try:
        connection.cursor()
        # print("Test Cursor")
    except Exception as e:
        print("The connection is broken.\n强制断开所有连接...")
        connection.close()
        # print("Reconnect...")
        connection = sqlite3.connect("transaction_db.db")
        # print("Connection reestablished.")
    finally:
        conn_lock.release()
        # print("Lock Released.")
        return connection

def set_db_file_path(path):
    global DB_FILE_PATH
    DB_FILE_PATH = path

def set_connection(connection):
    global DB_CONNECTION
    DB_CONNECTION = connection

def get_connection():
    global DB_CONNECTION
    return DB_CONNECTION

def set_cursor(c
