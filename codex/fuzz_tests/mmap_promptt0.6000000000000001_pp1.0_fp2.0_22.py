import mmap
# Test mmap.mmap
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
m.write("Hello world")
m.seek(0)
print(m.readline())
m.close()
f.close()
# Test mmap.mmap with size
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), mmap.PAGESIZE)
m[0:11] = "Hello world"
m.seek(0)
print(m.readline())
m.close()
f.close()
# Test mmap.mmap with offset
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), mmap.PAGESIZE, offset=mmap.PAGESIZE)
m[0:11] = "Hello world"
m.seek(0)
print(m.readline())
m.close()
f.close()
