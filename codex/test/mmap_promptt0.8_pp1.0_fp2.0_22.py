import mmap
# Test mmap.mmap(-1, size)
with open('test', 'wb') as f:
    f.write(b'a' * 4096)
with open('test', 'rb') as f:
    m = mmap.mmap(-1, mmap.PAGESIZE)
    m.write(f.read())

# Test mmap.mmap(-1, size, flags)
m = mmap.mmap(-1, mmap.PAGESIZE, mmap.MAP_ANON | mmap.MAP_PRIVATE)
