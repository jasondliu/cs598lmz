import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 4096)
print(len(m))
print(m.size())
m.close()

# Test mmap.mmap() with size 0
m = mmap.mmap(0, 0)
print(len(m))
print(m.size())
m.close()

# Test mmap.mmap() with offset
m = mmap.mmap(0, 4096, offset=0)
print(len(m))
print(m.size())
m.close()

# Test mmap.mmap() with offset and size
m = mmap.mmap(0, 4096, offset=0, size=4096)
print(len(m))
print(m.size())
m.close()

# Test mmap.mmap() with offset and size
m = mmap.mmap(0, 4096, offset=0, size=0)
print(len(m))
print(m.size())
m.close()

# Test mmap.mmap() with offset and size
m = mmap.
