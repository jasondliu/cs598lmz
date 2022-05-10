import mmap
# Test mmap.mmap()
#
# Create a memory-mapped file.
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]]) -> mmap object
#
# Create a new memory-mapped file object.
#
# fileno is an integer or long integer, giving the file descriptor of the
# file to be mapped, or -1. fileno is required unless length is 0.
#
# length is an integer or long integer, giving the length of the mapping.
#
# flags is an integer, giving the mmap flags to use. The default value is 0.
#
# prot is an integer, giving the desired memory protection. The default value
# is mmap.PROT_WRITE|mmap.PROT_READ.
#
# access is an integer, giving the desired access to the memory mapped file.
# The default value is mmap.ACCESS_DEFAULT.
#
# offset is an integer, giving the desired offset within the file. The default
# value is 0.
#
# The mmap() function is only available on Unix and Windows.
