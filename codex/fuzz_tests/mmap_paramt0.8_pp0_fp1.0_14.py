import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 65  # ASCII for 'A'
    m.flush()  # copy back to file
    print(m[:])

with open('test', 'rb') as f:
    data = f.read()
    print(data)

import mmap
import os

# Write a simple example file
with open('hello.txt', 'w') as f:
    f.write('Hello World!')

with open('hello.txt', 'r+b') as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b'Hello World!'
    mm.seek(0)  # rewind
    assert mm.read(5) == b'Hello'
    # read content via slice notation
    print(mm[6:])  # prints b'World!'
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b
