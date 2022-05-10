import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map using the file descriptor fileno, the
# optional flags and prot arguments are the same as the arguments to
# the Unix C function mmap(2).
#
# If length is 0, the maximum length of the map is the current size
# of the file when mmap is called.
#
# The access argument specifies the access to the memory, mmap
# currently supports the values ACCESS_DEFAULT, ACCESS_READ and
# ACCESS_WRITE.
#
# The offset argument is the offset into the file.
#
# If the file is extended while it is mmapped, the mmap will be
# extended as well.
#
# If the file is truncated while it is mmapped, the mmap will be
# reduced in size.
#
# If the file is closed while it is mmapped, the mmap will be
# invalidated.
#

