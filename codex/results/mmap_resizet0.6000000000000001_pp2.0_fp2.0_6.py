import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    #m.resize(1)
    m.resize(3)
    m[0] = b'a'
    m[1] = b'b'
    m[2] = b'c'
    print(m[:])
    m[:] = b'abc'
    print(m[:])
    m[:] = b'def'
    print(m[:])
    m.flush()
