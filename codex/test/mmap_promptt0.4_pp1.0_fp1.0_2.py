import mmap
# Test mmap.mmap()
#
# The mmap.mmap() function creates a new memory-mapped file object.
#
# Syntax
# Following is the syntax for mmap.mmap() method −
#
# mmap.mmap(fileno, length[, tagname[, access[, offset]]])
#
# Parameters
# fileno − This is the file descriptor of the file to be mapped.
#
# length − This is the length of the mapping.
#
# tagname − This is the name of the shared memory segment.
#
# access − This is the access mode for the mapping.
#
# offset − This is the offset in the file where the mapping starts.
#
# Return Value
# This method does not return any value.

# Example
# The following example shows the usage of mmap.mmap() method.

# Open a file
fd = os.open('foo.txt', os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, "This is test")

