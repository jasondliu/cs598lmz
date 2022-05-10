import mmap
# Test mmap.mmap.
m = mmap.mmap(-1, 1024)

m.write(b"Hello")
m.seek(0, 0)
s = m.readline()
print(s)
m.close()

# Test mmap.mmap.__getitem__.
# This has to be "r" rather than "r+" since it appears not to be possible
# to create a writeable mapping of a file opened as "r".
m = mmap.mmap(m.fileno(), 1024, access=m.ACCESS_READ)

s = m[3:8]
print(s)
m.close()

# Test mmap.mmap.find.
m = mmap.mmap(m.fileno(), 1024, access=m.ACCESS_READ)

n = m.find(b"lo")
print(n)
m.close()

# Test mmap.mmap.move + mmap.mmap.size.
m = mmap.mmap(m.fileno(), 1024) # r+

# Move to end of file
