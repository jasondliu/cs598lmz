import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

def thread_test(x):
    print(x)
    x.pop()
    print(x)

a = [3,4,5]

t = threading.Thread(target=thread_test, args=(a,))

t.start()
t.join()

# t = threading.Thread(target=thread_test, args=(6,))
# t.start()

print(a)
