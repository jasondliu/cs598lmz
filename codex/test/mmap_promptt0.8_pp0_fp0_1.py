import mmap
# Test mmap.mmap().  mmap is a module.  mmap() is a function.
# The mmap() function creates a new mmap object.

# The mmap() function needs a file descriptor to create a mmap object.
# You can get a file descriptor by opening a file.  You can open a file
# with the built-in open() function.  The open() function returns a file
# descriptor.

# A file descriptor is an integer.
# An mmap object is an object.
# An integer is not an object.
# See https://docs.python.org/3/library/mmap.html

# Open a file for reading.  "r" means reading.
fd = os.open('test_data.txt', os.O_RDONLY)

# fd is a file descriptor.
# fd is an integer.
print('fd=', fd)

# Mmap to create a memory-mapped file.
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
