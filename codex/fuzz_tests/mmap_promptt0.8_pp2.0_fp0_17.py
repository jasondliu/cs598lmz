import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 1024)
m.write(b"Hello World")
# memmove()
m.seek(0)
m.read()
m.seek(0)
m.write(b"Hello World Second")
m.seek(0)
m.read()
# Test mmap.mmap(file.fileno())
f = open("tmp.txt", "r+")
m = mmap.mmap(f.fileno(), 1024)
m.write(b"Hello World Second")
m.seek(0)
m.read()
m.close()
f.close()

# Test mmap.mmap(fd, length, tagname, access=mmap.ACCESS_WRITE)
f = open("tmp.txt", "w+")
f.close()
f = open("tmp.txt", "r+")
m = mmap.mmap(f.fileno(), 1024, tagname="test", access=mmap.ACCESS_WRITE)

m.write(b"Hello World Second")
m.seek(
