import ctypes
ctypes.cast(0, ctypes.py_object).value = 'spam'

ctypes.cast(id(sys), ctypes.c_void_p).value

import struct
struct.pack('>L', 10240099)
struct.unpack('>L', b'\x00\x9c@c')

b = struct.pack('>L', 10240099)
import binascii
binascii.hexlify(b)
binascii.unhexlify(b'\x00\x9c@c')

a = 'I am a string'
import sys
a = sys.intern(a)
b = 'I am a string'
a is b

import array
# array.array('I', (a for a in range(10)))
# array.array('I', [a for a in range(10)])
# array.array('I', (a for a in range(10))) == array.array('I', [a for a in range(10)])

from collections import deque

# d = deque(['task1
