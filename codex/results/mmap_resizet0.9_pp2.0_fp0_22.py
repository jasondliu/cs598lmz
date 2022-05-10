import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # change this line to inspect m's behavior
    m.close()
    assert a == b''
# del a



fd = open('test', 'r+b')
m = mmap.mmap(fd.fileno(), 0)
fd.truncate()
for i in range(0, 100):
    try:
        m[i]
    except ValueError:
        pass
#1/0


# IOWrapper.close does the same thing.

import io
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

fd = open('test', 'rb')
fd_wrapper = io.open(fd.fileno(), 'rb')

m = mmap.mmap(fd.fileno(), 0)
fd_wrapper.close()

m[2]
a = m[:]  # change this line to inspect m's behavior
m.close()
# del a
# del m


import fcntl

# This test fails early, because upon the execution of fcntl.lock
