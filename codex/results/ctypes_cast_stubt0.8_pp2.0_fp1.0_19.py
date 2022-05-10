import ctypes
ctypes.cast(1, ctypes.py_object)

import sys
sys.getrefcount(1)

ctypes.cast(1, ctypes.py_object)

sys.getrefcount(1)

#MemoryView

s = b'Hello World'

mv = memoryview(s)

#Operation on mv and s is identical

mv[0] = b'J'

mv[-1]

s

#Without memoryview, changing s involves creating a copy

s = bytearray(b'Hello World')

s[0] = ord(b'J')

#With memoryview, we can share data between the bytes, list, memoryview, and array

#The memoryview allows Python to handle mutable and immutable byte sequences efficiently

#Normalization

#Unicode normalization ensures that equivalent text uses the same sequence of code points

s1 = 'cafe\u0301'

s2 = 'cafe\u0301'

s1 == s2

#The two strings are different

#s1
