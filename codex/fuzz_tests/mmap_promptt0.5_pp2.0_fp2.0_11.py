import mmap
# Test mmap.mmap()

with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    m.seek(0)
    m.write(b'0123456789abcdef')
    m.seek(0)
    print(m.readline())
    m.close()

with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m.close()

with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), mmap.PAGESIZE, access=mmap.ACCESS_WRITE)
    print(len(m))
    print(m[:])
    m.close()

with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(
