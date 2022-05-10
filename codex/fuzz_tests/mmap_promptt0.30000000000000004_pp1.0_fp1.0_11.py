import mmap
# Test mmap.mmap
f = open("test.txt", "r")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print m.readline()
print m.readline()
m.close()
f.close()

# Test mmap.mmap(offset)
f = open("test.txt", "r")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, offset=10)
print m.readline()
print m.readline()
m.close()
f.close()

# Test mmap.mmap(offset, size)
f = open("test.txt", "r")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, offset=10, size=10)
print m.readline()
print m.readline()
m.close()
f.close()

# Test mmap.mmap(offset, size, tagname)
f = open("test.txt", "r")
m
