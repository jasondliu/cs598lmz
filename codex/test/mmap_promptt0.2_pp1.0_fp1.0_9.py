import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is an integer file descriptor of the file to be mapped.
# length is the number of bytes to map.
# flags is one of MAP_SHARED, MAP_PRIVATE, MAP_ANONYMOUS, or the bitwise OR of these values.
# prot is the desired memory protection of the mapping. It is one of PROT_EXEC, PROT_READ, PROT_WRITE, or the bitwise OR of these values.
# access is either MAP_SHARED or MAP_PRIVATE, as for the flags argument.
# offset is the offset (in bytes) of the first mapped page relative to the start of the file.
#
# The return value is a mmap object.
#
# The mmap object can be treated as a mutable string.
#
# The mmap object also has some methods that are similar to those found on regular Python file objects.
#
# The mmap object has the following methods:
#
# mmap.close()

