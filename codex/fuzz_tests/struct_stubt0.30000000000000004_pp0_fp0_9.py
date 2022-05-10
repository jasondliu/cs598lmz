from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '<')
s.size

s.pack(1)

s.unpack(b'\x01\x00\x00\x00')

s.unpack(b'\x01\x00\x00\x00')[0]

import array
nums = array.array('i', [1, 2, 3, 4])
nums

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
a

import os
fd = os.open('data.bin', os.O_RDWR | os.O_CREAT)

with os.fdopen(fd, 'w+b') as f:
    f.write(b'Hello World')
    f.flush()
    os.lseek(fd, 0, 0)
    data = f.read()

data

os.remove('data.bin')

with open('data.bin', 'wb') as f:
    f.write(b'Hello World')

with open('
