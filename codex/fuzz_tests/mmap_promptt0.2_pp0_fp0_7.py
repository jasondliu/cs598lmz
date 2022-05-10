import mmap
# Test mmap.mmap
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map using the file descriptor fileno,
# the size of the mapping is given by length, and the optional
# flags and prot arguments can be used to control the
# access to the mapping.
#
# The access argument is a bitwise OR of mmap.ACCESS_* values
# specifying the desired memory access:
#
# mmap.ACCESS_READ
# mmap.ACCESS_WRITE
# mmap.ACCESS_COPY
#
# The offset argument specifies the offset (in bytes) from the
# beginning of the file where the mapping is to begin.
#
# The flags argument is a bitwise OR of mmap.MAP_* values
# specifying the desired behavior of the mapping:
#
# mmap.MAP_SHARED
# mmap.MAP_PRIVATE
# mmap.MAP_ANONYMOUS
# mmap.MAP_ANON
# mmap.MAP_FIXED
#
# The
