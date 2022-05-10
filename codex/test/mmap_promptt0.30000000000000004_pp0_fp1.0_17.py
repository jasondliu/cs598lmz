import mmap
# Test mmap.mmap.read_byte
with open("/proc/self/stat", "rb") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
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
        print(m.read_byte())
        print(m.read_byte())
        print(m.read_byte())
