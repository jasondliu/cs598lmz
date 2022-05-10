import mmap
# Test mmap.mmap with offset
m = mmap.mmap(0, 1, "a", mmap.ACCESS_READ)
m.seek(1024)
m.read_byte()
m.close()

# Test mmap.mmap with offset and size
m = mmap.mmap(0, 1024, "a", mmap.ACCESS_READ)
m.read_byte()
m.close()

# Test mmap.mmap with offset, size, and tagname
m = mmap.mmap(0, 1024, "a", mmap.ACCESS_READ)
m.read_byte()
m.close()

# Test mmap.mmap with offset, size, tagname, and access
m = mmap.mmap(0, 1024, "a", mmap.ACCESS_READ)
m.read_byte()
m.close()

# Test mmap.mmap with offset, size, tagname, access, and handle
m = mmap.mmap(0, 1024, "a", mmap.ACCESS_READ)
m.read_byte()

