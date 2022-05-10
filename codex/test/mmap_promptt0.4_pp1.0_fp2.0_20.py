import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 100, "test_mmap")
m.write("Hello World!")
m.seek(0)
