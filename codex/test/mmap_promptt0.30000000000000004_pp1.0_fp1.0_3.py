import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 1, "test", mmap.ACCESS_WRITE)
m.write("a")
m.close()

# Test mmap.mmap(-1, ...)
m = mmap.mmap(-1, 1, "test", mmap.ACCESS_WRITE)
m.write("a")
m.close()

# Test mmap.mmap(<fd>, ...)
f = open("test", "w+")
m = mmap.mmap(f.fileno(), 1, "test", mmap.ACCESS_WRITE)
m.write("a")
m.close()

# Test mmap.mmap(<fd>, ..., offset)
f = open("test", "w+")
m = mmap.mmap(f.fileno(), 1, "test", mmap.ACCESS_WRITE, offset=1)
m.write("a")
m.close()
