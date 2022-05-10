import mmap
# Test mmap.mmap.read_byte
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read_byte())
    m.close()

# Test mmap.mmap.readline
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.readline())
    m.close()

# Test mmap.mmap.readlines
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.readlines())
    m.close()

# Test mmap.mmap.seek
