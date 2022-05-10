import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, num INTEGER, data TEXT)')
cursor.execute('INSERT INTO test(num, data) VALUES(1, "hello")')
cursor.execute('INSERT INTO test(num, data) VALUES(2, "world")')
cursor.execute('SELECT * FROM test')
print(cursor.fetchall())
conn.close()

# Test ctypes.util.find_library
print(ctypes.util.find_library('c'))

# Test threading.Thread
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))

thread_1 = threading.Thread(target=print_time, args=("Thread-1", 2,))
