import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 12)
m.write("Hello World!")
m.seek(0)
print m.readline()
m.close()

# Test mmap.mmap(fd, size)
m = mmap.mmap(m.fileno(), 12)
m.write("Hello World!")
m.seek(0)
print m.readline()
m.close()
