import mmap
# Test mmap.mmap(0, size)
m = mmap.mmap(0, 100)
m[0] = 'a'
m[1] = 'b'
m.seek(0)
print m.readline()
m.close()

# Test mmap.mmap(0, size, access=mmap.ACCESS_WRITE)
m = mmap.mmap(0, 100, mmap.ACCESS_WRITE)
m[0] = 'a'
m[1] = 'b'
m.seek(0)
print m.readline()
m.close()

# Test mmap.mmap(-1, size)
m = mmap.mmap(-1, 100)
m[0] = 'a'
m[1] = 'b'
m.seek(0)
print m.readline()
m.close()

# Test mmap.mmap(-1, size, access=mmap.ACCESS_WRITE)
m = mmap.mmap(-1, 100, mmap.ACCESS_WRITE)
m[0]
