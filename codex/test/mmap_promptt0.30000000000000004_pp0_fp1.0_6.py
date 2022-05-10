import mmap
# Test mmap.mmap()
f = open(filename, "r+")
m = mmap.mmap(f.fileno(), 0)
print("mmap.mmap():", m.readline())
m.close()
f.close()

# Test mmap.mmap() with a file-like object
f = open(filename, "r+")
m = mmap.mmap(f.fileno(), 0)
print("mmap.mmap():", m.readline())
m.close()
f.close()

# Test mmap.mmap() with a file-like object and offset
f = open(filename, "r+")
m = mmap.mmap(f.fileno(), 0, offset=10)
print("mmap.mmap():", m.readline())
m.close()
f.close()

# Test mmap.mmap() with a file-like object, offset, and length
