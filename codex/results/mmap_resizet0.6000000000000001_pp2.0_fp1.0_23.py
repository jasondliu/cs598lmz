import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)
    m[0] = b'\x00'
    m.close()
    f.truncate()
    b = m[:]

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)
    m[0] = b'\x00'
    m.close()
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    b = m[:]
