import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('/home/pi/Desktop/test.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value INTEGER)''')
#c.execute('''INSERT INTO test (value) VALUES (?)''', (1,))
#conn.commit()
#conn.close()

# Test ctypes.util.find_library()
#libc = ctypes.util.find_library('c')
#print(libc)

# Test ctypes.CDLL()
#libc = ctypes.CDLL(libc)
#print(libc)

# Test ctypes.CDLL().malloc()
#malloc = libc.malloc
#malloc.restype = ctypes.c_void_p
#malloc.argtypes = [ctypes.c_size_t]
#ptr = malloc(4)
#print(ptr)

# Test ctypes.cast()
#ptr = c
