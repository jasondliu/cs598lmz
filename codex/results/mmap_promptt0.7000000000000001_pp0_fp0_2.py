import mmap
# Test mmap.mmap() call
m = mmap.mmap(-1, 1024, "mmap_test")
# Test m.write()
m.write("Hello world")
# Test m.read()
m.seek(0)
print m.read(11)
