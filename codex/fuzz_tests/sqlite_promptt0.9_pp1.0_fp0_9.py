import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.cursor, successfully

# TODO: is JDK can success?

def find_db_path():
    db_path = None
    try:
        db_path = ctypes.util.find_library('libsglserver.so')
    except Exception as e:
        print(e)
    finally:
        return db_path

def test():
    db = sqlite3.connect(find_db_path())
    cursor = db.cursor()

    cursor.execute("SELECT * FROM XResParam")
    values = cursor.fetchall()
    print(values)

if __name__ == '__main__':
    test()
