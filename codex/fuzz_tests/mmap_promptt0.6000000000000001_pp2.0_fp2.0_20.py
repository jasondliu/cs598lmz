import mmap
# Test mmap.mmap() for read-write access
m = mmap.mmap(-1, 1000000)
m.write(b"Hello Python!\n")
print(m.readline())
m.close()

# Test mmap.mmap() for read-only access
m = mmap.mmap(-1, 1000000, access=mmap.ACCESS_READ)
print(m.readline())
m.close()

# Test mmap.mmap() for write-only access
m = mmap.mmap(-1, 1000000, access=mmap.ACCESS_WRITE)
m.write(b"Hello Python!\n")
m.close()
