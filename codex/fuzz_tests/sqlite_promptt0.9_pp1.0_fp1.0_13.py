import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect if it is faster on my end

# get the crc32
# https://stackoverflow.com/questions/11444434/python-how-to-get-crc32-in-hex-with-core-python
# solution by vzx

# workaround for unpacking a string to a truncated c_byte array
# https://stackoverflow.com/questions/6083822/unpack-a-string-into-a-c-type-array
# answer by Collin Anderson

# size_t in ctypes
# https://stackoverflow.com/questions/24700935/python-ctypes-32-bit-and-64-bit-integers
# https://docs.python.org/3/library/ctypes.html#fundamental-data-types

# buffer protocol
# https://docs.python.org/3.7/c-api/buffer.html
# https://docs.python.org/3/c-api/memoryview.html

# reading bytes into a buffer
# https://docs.python.org/3.7/library
