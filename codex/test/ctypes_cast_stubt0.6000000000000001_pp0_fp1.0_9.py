import ctypes
ctypes.cast(12, ctypes.py_object)

# Using the "memoryview" object
m = memoryview(b"abcefg")
m
m[1]
m[-1]
m[1:4]

# The "bytearray" object
a = bytearray(b"abcdefg")
a
a[1]
a[1] = ord('z')
a
a[1:3]
a[1:3] = b"xy"
a
a[1:3] = memoryview(b"xy")
a

# The "bytes" object
a = b"abcdefg"
a
a[1]
try:
    a[1] = ord('z')
except TypeError as e:
    print(e)
a[1:3]
