import mmap
# Test mmap.mmap(fileno, length)
m = mmap.mmap(-1, 1)
m.write_byte(b'\0')
m.seek(0)
print(m.read_byte())
m.close()

# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
m = mmap.mmap(-1, 1, mmap.ACCESS_WRITE)
m.write_byte(b'\0')
m.seek(0)
print(m.read_byte())
m.close()

# Test mmap.mmap(fileno, length, access=mmap.ACCESS_READ)
m = mmap.mmap(-1, 1, mmap.ACCESS_READ)
m.write_byte(b'\0')
m.seek(0)
print(m.read_byte())
m.close()

# Test mmap.mmap(fileno, length, access=mmap.ACCESS_COPY)
m = mmap.mmap(-1, 1, mmap.
