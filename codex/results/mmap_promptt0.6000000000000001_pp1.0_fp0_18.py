import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 1, "test")
print m.read(1)
m.close()

# Test mmap.mmap() with fileno
f = open("test", "r+")
m = mmap.mmap(f.fileno(), 1)
print m.read(1)
m.close()
f.close()

# Test mmap.mmap() with file object
f = open("test", "r+")
m = mmap.mmap(f.fileno(), 1)
print m.read(1)
m.close()
f.close()

# Test mmap.mmap() with a negative length
try:
    m = mmap.mmap(-1, 1)
except ValueError:
    print "Caught ValueError"

# Test mmap.mmap() with a size of 0
m = mmap.mmap(0, 0)
print m.size()
m.close()

# Test mmap.mmap() with offset
m = mmap.mmap(0, 1,
