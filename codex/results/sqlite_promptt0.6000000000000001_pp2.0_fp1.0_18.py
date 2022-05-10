import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect(':memory:')

# Test ctypes.util.find_library
lib = ctypes.util.find_library('c')

# Test threading.Thread
t = threading.Thread(target=lambda: None)

# Test threading.Lock
l = threading.Lock()

# Test ctypes.CDLL
libc = ctypes.CDLL(lib)

# Test ctypes.CFUNCTYPE
f = ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x)

# Test ctypes.c_int and ctypes.pointer
i = ctypes.c_int(1)
ip = ctypes.pointer(i)

# Test ctypes.c_char_p
cp = ctypes.c_char_p(b'hello')
