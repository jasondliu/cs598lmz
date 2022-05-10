import mmap
# Test mmap.mmap
m = mmap.mmap(0, 1024)
m.write("Hello, world!")
