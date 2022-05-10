import mmap
# Test mmap.mmap().
m = mmap.mmap(0, 1, "i'm a little teapot")
# Test mmap.mmap.size().
print(m.size())
# Test mmap.mmap.resize().
m.resize(2)
# Test mmap.mmap.tell().
print(m.tell())
# Test mmap.mmap.close().
m.close()
