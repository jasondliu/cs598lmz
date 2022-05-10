import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('database/masterDB.sqlite3',check_same_thread=False)
# Test sqlite3.connect('database/masterDB.sqlite3') pour test

def db_create_connection():
    return sqlite3.connect('database/masterDB.sqlite3',check_same_thread=False)

def db_insert(query):
    print("[db_insert] query : {}".format(query))
    p = db_create_connection()
    try:
        cursor = p.cursor()
        cursor.execute(query)
        p.commit()
        print("[db_insert] Enregistrement effectué")
    except:
        print("[db_insert] Erreur d'enregistrement")
    finally:
        p.close()

def db_read(query):
    print("[db_read] query : {}".format(query))
    p = db_create_connection()
