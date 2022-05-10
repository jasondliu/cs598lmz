import mmap
# Test mmap.mmap.read_byte
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_READ)
    m.read_byte()
    m.read_byte()
    m.read_byte()
    m.close()
# Test mmap.mmap.read
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_READ)
    m.read(3)
    m.close()
# Test mmap.mmap.read1
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_READ)
    m.read1(3)
    m.close()
# Test mmap.mmap.readline
with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 1, access=
