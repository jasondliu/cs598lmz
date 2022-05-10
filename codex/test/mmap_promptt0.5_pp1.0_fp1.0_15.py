import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 12)
m.write("Hello World!")
