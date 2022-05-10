import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()

import mmap

with open('test', 'rb+') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

import mmap

with open('test', 'rb+') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()

import mmap

with open('test', 'wb+') as f:
    f.write(bytes(1))
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

import mmap

with open('test', 'wb+') as f
