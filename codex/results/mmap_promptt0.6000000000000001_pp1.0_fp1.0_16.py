import mmap
# Test mmap.mmap.read_byte

with open("/dev/urandom", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read_byte())
