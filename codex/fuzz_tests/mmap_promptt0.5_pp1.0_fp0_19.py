import mmap
# Test mmap.mmap()
data = open("/dev/mem", "rb").read()
assert data == mmap.mmap(-1, len(data), "", mmap.MAP_PRIVATE, "/dev/mem")

# Test mmap.mmap() with an offset
data = open("/dev/mem", "rb").read()
assert data == mmap.mmap(-1, len(data), "", mmap.MAP_PRIVATE, "/dev/mem", 0)

# Test mmap.mmap() with a file
data = open("/dev/mem", "rb").read()
assert data == mmap.mmap(-1, len(data), "", mmap.MAP_PRIVATE, open("/dev/mem", "rb"))

# Test mmap.mmap() with a file and an offset
data = open("/dev/mem", "rb").read()
assert data == mmap.mmap(-1, len(data), "", mmap.MAP_PRIVATE, open("/dev/mem", "rb"), 0)

# Test mmap.mmap()
