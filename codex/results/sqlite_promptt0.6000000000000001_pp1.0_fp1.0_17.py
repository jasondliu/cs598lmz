import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections

# Test sqlite3.connections

import sqlite3

def test():
    conns = []
    for i in range(10):
        conns.append(sqlite3.connect(":memory:"))
    for conn in conns:
        conn.close()

def test_threads():
    global threads_done
    threads_done = 0
    def worker():
        global threads_done
        test()
        threads_done += 1

    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=worker))
    for th in threads:
        th.start()
    while threads_done < len(threads):
        pass

test()
test_threads()

print("Done.")
