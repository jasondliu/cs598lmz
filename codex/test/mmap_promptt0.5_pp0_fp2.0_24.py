import mmap
# Test mmap.mmap
m = mmap.mmap(0, 10, "MySharedMem")
m[0:5] = "Hello"
m.seek(0)
