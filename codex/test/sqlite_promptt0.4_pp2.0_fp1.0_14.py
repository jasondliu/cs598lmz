import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def thread_func(id):
    print("[%d] thread start" % id)
    try:
        conn = sqlite3.connect('test.db')
    except Exception as e:
        print("[%d] thread sqlite3.connect() exception: %s" % (id, e))
        return
    print("[%d] thread sqlite3.connect() success" % id)
    conn.close()

def main():
    for i in range(10):
        t = threading.Thread(target=thread_func, args=(i,))
        t.start()

if __name__ == '__main__':
    main()
