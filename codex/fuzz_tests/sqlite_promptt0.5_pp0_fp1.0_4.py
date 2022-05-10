import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('/home/pi/Desktop/test.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE test (id int)""")
# c.execute("INSERT INTO test VALUES (1)")
# conn.commit()
# conn.close()
# print("test.db created")

# Test ctypes library
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# libc.printf("Hello World!\n")

# Test threading
def print_hello():
    print("Hello")

t1 = threading.Thread(target=print_hello)
t2 = threading.Thread(target=print_hello)
t1.start()
t2.start()
t1.join()
t2.join()
