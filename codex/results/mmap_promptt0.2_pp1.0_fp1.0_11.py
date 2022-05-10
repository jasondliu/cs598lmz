import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is the file descriptor of the file to be mapped.
# length is the number of bytes to map.
# flags is one of mmap.MAP_SHARED, mmap.MAP_PRIVATE, mmap.MAP_ANONYMOUS,
# mmap.MAP_ANON, or mmap.MAP_32BIT.
# prot is the desired memory protection of the mapping.
# access is the desired memory access of the mapping.
# offset is the offset into the file to start the mapping.
#
# The return value is a mmap object.
#
# The mmap object behaves like a file object, except that some of the
# methods are unavailable.
#
# The mmap object also has some methods and attributes unique to mmap objects.
#
# The mmap object has the following methods:
#
# close()
# Flush changes and close the mapping.
#
# find(sub[, start[, end]])
# Return the
