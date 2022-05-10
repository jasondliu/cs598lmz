import mmap
# Test mmap.mmap.readline()

with open("/tmp/test.txt", "wb") as f:
    f.write(b"hello\nworld\n")

with open("/tmp/test.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.readline())
    print(m.readline())
    print(m.readline())
    print(m.readline())
    m.close()

with open("/tmp/test.txt", "wb") as f:
    f.write(b"hello\nworld\n")

with open("/tmp/test.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.readline(4))
    print(m.readline(4))
    print(m.readline(4))
    print(m.readline(4))
    m.close()

with
