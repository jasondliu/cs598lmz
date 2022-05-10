import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 0, "MySharedMemory", mmap.ACCESS_WRITE)
m[0:13] = "Hello, World!"
m.close()

# Test mmap.mmap(-1, ...)
m = mmap.mmap(-1, 13, "MySharedMemory", mmap.ACCESS_WRITE)
m[0:13] = "Hello, World!"
m.close()

# Test mmap.mmap(fileno, ...)
f = open("MySharedMemory", "w+")
m = mmap.mmap(f.fileno(), 13, access=mmap.ACCESS_WRITE)
m[0:13] = "Hello, World!"
m.close()
f.close()

# Test copy-on-write mmap
f = open("MySharedMemory", "w+")
m = mmap.mmap(f.fileno(), 13, access=mmap.ACCESS_COPY)
m[0:13] = "Hello, World!"
m.
