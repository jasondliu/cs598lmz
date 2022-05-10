import mmap
# Test mmap.mmap.read() with 0-byte length.

m = mmap.mmap(-1, 0)
m.write(b"Testing...\n")
m.seek(0)
# 1st read: 0-byte read
m.read(0)
# 2nd read: read the whole mmap
print("mmap.read(0) succeeded")
m.read()

# Test mmap.mmap.read() with negative length.
m.seek(0)
m.read(-1)
m.read()
print("mmap.read(-1) succeeded")

# Test mmap.mmap.read_byte() with negative length.
m.seek(0)
m.read_byte(-1)
m.read()
print("mmap.read_byte(-1) succeeded")

# Test mmap.mmap.readline() with negative length.
m.seek(0)
m.readline(-1)
m.read()
print("mmap.readline(-1) succeeded")

# Test mmap.mmap.readlines() with negative length.

