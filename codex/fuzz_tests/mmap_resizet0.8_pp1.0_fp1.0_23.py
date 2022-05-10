import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[0:]
    c = m[:1]
    m.close()

with open('test', 'wb') as f:
    f.write(bytes(4))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m[:] = b''
    m.close()

with open('test', 'wb') as f:
    f.write(bytes(8))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m[:8] = b''
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(5)
    m[5:] = b''
    m.close()

with open('test', 'r+b') as
