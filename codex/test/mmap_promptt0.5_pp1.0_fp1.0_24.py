import mmap
# Test mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_WRITE)
# Test mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_COPY)
# Test mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_READ)

import sys
import os

# Test that mmap works with a file opened in append mode
f = open('test.dat', 'w+')
f.write('a' * 10)
f.close()
f = open('test.dat', 'a+')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m.write('b' * 10)
m.close()
f.close()
f = open('test.dat', 'rb')
buf = f.read()
f.close()
if buf != 'a' * 10 + 'b' * 10:
    raise RuntimeError('append mode')

# Test mmap.move
