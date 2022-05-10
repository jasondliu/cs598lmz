import mmap
# Test mmap.mmap
with open('test.txt', 'w+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'abc')
    m.seek(0)
    print(m.read(3))
    m.close()

# Test mmap.mmap(fileno, length, flags, prot, access, offset)
with open('test.txt', 'w+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    m.write(b'abc')
    m.seek(0)
    print(m.read(3))
    m.close()

# Test mmap.mmap(fileno, length, flags, prot, access, offset)
with open('test.txt', 'w+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'abc')
    m.seek(0)
    print(m.
