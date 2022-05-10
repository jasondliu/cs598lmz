import mmap
# Test mmap.mmap(0, 0).tell()
with mmap.mmap(0, 0) as m:
    print(m.tell())

# Test mmap.mmap(-1, 0).tell()
with mmap.mmap(-1, 0) as m:
    print(m.tell())

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_READ).tell()
with mmap.mmap(-1, 0, access=mmap.ACCESS_READ) as m:
    print(m.tell())

# Test mmap.mmap(0, 0, access=mmap.ACCESS_READ).tell()
with mmap.mmap(0, 0, access=mmap.ACCESS_READ) as m:
    print(m.tell())

# Test mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE).tell()
with mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE) as m:
    print(m.tell())

# Test mmap.
