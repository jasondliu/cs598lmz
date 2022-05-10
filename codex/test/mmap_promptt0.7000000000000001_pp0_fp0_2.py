import mmap
# Test mmap.mmap() call
m = mmap.mmap(-1, 1024, "mmap_test")
# Test m.write()
m.write("Hello world")
