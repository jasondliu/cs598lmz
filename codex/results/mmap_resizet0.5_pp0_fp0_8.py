import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'rb') as f:
    a = f.read()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno
