import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 10, access=mmap.ACCESS_WRITE)
m.write(b'0123456789')
m.close()

# Test mmap.mmap()
m = mmap.mmap(-1, 10, access=mmap.ACCESS_READ)
m.write(b'0123456789')
m.close()

# Test mmap.mmap()
m = mmap.mmap(-1, 10, access=mmap.ACCESS_COPY)
m.write(b'0123456789')
m.close()

# Test mmap.mmap()
m = mmap.mmap(-1, 10, access=mmap.ACCESS_DEFAULT)
m.write(b'0123456789')
m.close()

# Test mmap.mmap()
m = mmap.mmap(-1, 10, access=0)
m.write(b'0123456789')
m.close()

# Test mmap.mmap()

