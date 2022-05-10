import mmap
# Test mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE)
# See the following for more info:
# https://docs.python.org/2/library/mmap.html

map = mmap.mmap(-1,1024,access=mmap.ACCESS_WRITE) # The access=mmap.ACCESS_WRITE is default
# We are creating a shared memory map of size 1024 bytes (1 KB) in memory.
# The fileno=-1 means that we are creating our own anonymous file-like object.
# It is not associated with any actual file on disk.
# The file descriptor is -1.

# We have created a mmap object.  We can treat it like a file.
map.write("Hello shared memory world!\n")
map.seek(0)
print "This is the content of our mmap object:"
print map.readline()

# The mmap object is a file-like object that is backed by a shared memory
# segment.  It is not a mutable python string.
# We can convert it to a mutable python string like this:

