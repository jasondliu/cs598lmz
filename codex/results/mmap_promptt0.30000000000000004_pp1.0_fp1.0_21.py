import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 1024, "MySharedMemory", mmap.ACCESS_READ)
print(m[0:10])

# Test mmap.mmap()
m = mmap.mmap(0, 1024, "MySharedMemory", mmap.ACCESS_WRITE)
m[0:10] = b"Hello world"

# Test mmap.mmap()
m = mmap.mmap(0, 1024, "MySharedMemory")
print(m[0:10])
m.close()

# Test mmap.mmap()
m = mmap.mmap(0, 1024, "MySharedMemory", mmap.ACCESS_WRITE)
m[0:10] = b"Hello world"
m.close()

# Test mmap.mmap()
m = mmap.mmap(0, 1024, "MySharedMemory")
print(m[0:10])
m.close()

# Test mmap.mmap()
m = mmap.mmap(0, 1024, "My
