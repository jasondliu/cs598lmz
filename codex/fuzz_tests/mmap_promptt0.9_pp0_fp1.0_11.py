import mmap
# Test mmap.mmap(-1, 1024)
buf = mmap.mmap(-1, 1024)
print(type(buf))
# Test memoryview(mmap.mmap(-1, 1024))
memoryview(mmap.mmap(-1, 1024))
