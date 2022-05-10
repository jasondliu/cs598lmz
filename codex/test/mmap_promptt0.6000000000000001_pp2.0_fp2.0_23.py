import mmap
# Test mmap.mmap()
import os
import sys
import time

# Test that the mmap module can handle files opened in append mode
# (issue #14091).

# Create the file
with open('mmap_append.txt', 'w') as f:
    f.write('Hello, world.')

with open('mmap_append.txt', 'a') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write('bye')
    m.seek(0)
    m.write('HELLO')
    m.close()

with open('mmap_append.txt', 'r') as f:
    assert f.read() == 'HELLO, world.bye'

os.remove('mmap_append.txt')

# Test that the mmap module can handle files opened in read/write mode
