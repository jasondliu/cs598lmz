from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x9a\x99\x99\x99\x99\x99\xf1?'))

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)

import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))

del header
del img

import os
print(os.getcwd())

import sys
print(sys.path)

import string
print(string.ascii_letters)
print(string.ascii
