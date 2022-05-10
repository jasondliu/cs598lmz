from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

import threading
d = threading.local()
d.x = 1

import binascii
s = 'This is the string.'
b = s.encode('utf-16')
binascii.b2a_hex(b)
binascii.crc32(b)

import sys
for i in range(10 ** 5):
    print(sys.getrefcount(i))

class C(object):
    def m(self):
        pass

c = C()
c.m()

c = C()
getattr(c, 'm')()

import os
import time
dirname = 'dir'
try:
    os.mkdir(dirname)
except FileExistsError:
    pass
filename = os.path.join(dirname, 'file')
with open(filename, 'wt') as f:
    f.write('contents')
time.sleep(10)
os.remove(filename)
os.rmdir(dirname)


