import mmap
# Test mmap.mmap.read_byte()

with open("/tmp/mmap_test", "wb") as f:
    f.write(b"Hello, world!")

with open("/tmp/mmap_test", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
