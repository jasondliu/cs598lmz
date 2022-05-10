import mmap
# Test mmap.mmap.resize():

import mmap
import os

filename = 'tempfile'

f = open(filename, 'w+b')
f.write(b'abcdefghi')
f.close()

f = open(filename, 'r+b')
f.seek(3)
m = mmap.mmap(f.fileno(), 5)
m.resize(3)
m.close()
f.close()

f = open(filename, 'rb')
print(f.read())
f.close()

os.remove(filename)

# Test mmap.mmap(-1, size):

import mmap
import os

filename = 'tempfile'

f = open(filename, 'w+b')
f.write(b'abcdefghi')
f.close()

f = open(filename, 'r+b')
f.seek(3)
m = mmap.mmap(-1, 5)
m.close()
f.close()

f = open(filename, 'rb')
