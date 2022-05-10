import mmap
# Test mmap.mmap
m = mmap.mmap(0, 10, "MySharedMem")
m[0:5] = "Hello"
m.seek(0)
print m.read(5)

m[6:11] = "World"
m.seek(6)
print m.read(5)

m.close()

# Test mmap.mmap(fd)
f = open("foo", "r+b")
m = mmap.mmap(f.fileno(), 10)
m[0:5] = "Hello"
m.seek(0)
print m.read(5)

m[6:11] = "World"
m.seek(6)
print m.read(5)

m.close()
f.close()
