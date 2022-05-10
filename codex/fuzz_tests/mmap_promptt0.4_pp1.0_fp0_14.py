import mmap
# Test mmap.mmap()

# Test for read-write access
m = mmap.mmap(-1, 16, access=mmap.ACCESS_WRITE)
m.write(b"abcdefghijklmnop")
m.seek(0)
print(m.read(1))
print(m.read(1))
m.seek(0)
print(m.read(16))
m.close()

# Test for read-only access
m = mmap.mmap(-1, 16, access=mmap.ACCESS_READ)
m.write(b"abcdefghijklmnop")
m.seek(0)
print(m.read(1))
print(m.read(1))
m.seek(0)
print(m.read(16))
m.close()

# Test for copy-on-write access
m = mmap.mmap(-1, 16, access=mmap.ACCESS_COPY)
m.write(b"abcdefghijklmnop")
m.seek(0)
print(m.read(1))
