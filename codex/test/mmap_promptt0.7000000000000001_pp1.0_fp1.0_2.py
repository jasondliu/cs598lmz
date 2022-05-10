import mmap
# Test mmap.mmap()
# Create a new mmap object by specifying the file descriptor fd,
# the desired memory access, and the offset and size.
# Return a mmap object.
#

# https://docs.python.org/3/library/mmap.html

# specify the file descriptor fd.
f = os.open("./file.txt", os.O_RDWR)
print(f)
# specify the desired memory access.
# mmap.ACCESS_READ: read-only.
# mmap.ACCESS_WRITE: read and write. 

# specify the offset and size.
m = mmap.mmap(f, 0, mmap.ACCESS_WRITE)
print(m)
# read the whole file.
print(m.read(10))
# get the current position of the file pointer.
print(m.tell())
# seek to a position in the file.
m.seek(0)
# write something to the file.
m.write(b'0123456789abcdef')
