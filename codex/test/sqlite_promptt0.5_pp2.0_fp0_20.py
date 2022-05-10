import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# conn.close()

# Get the path of libz.so
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.malloc.restype = ctypes.c_void_p

# Create a new memory block
block = libc.malloc(100)

# Write "Hello, World!" to the memory block
libc.memcpy(block, "Hello World!", 13)

# Create a new Python string from the memory block
# (Don't do this in real code! Use the ctypes buffer interface instead)
s = ctypes.string_at(block, 13)

# Print the string
