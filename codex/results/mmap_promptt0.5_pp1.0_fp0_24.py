import mmap
# Test mmap.mmap:
m = mmap.mmap(-1, 1024)
m.write("1234567890")
assert m.size() == 10
m.seek(0)
assert m.read(5) == "12345"
m.close()

# Test mmap.mmap with a file descriptor:
fd = os.open(__file__, os.O_RDONLY)
m = mmap.mmap(fd, 1024, access=mmap.ACCESS_READ)
assert m.read(5) == "#!/usr"
m.close()
os.close(fd)

# Test mmap.mmap with a file-like object:
f = open(__file__, 'rb')
m = mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)
assert m.read(5) == "#!/usr"
m.close()
f.close()

# Test mmap.mmap with an integer file descriptor:
import os, mmap
f = open(__file__, 'r+')
m = mmap.
