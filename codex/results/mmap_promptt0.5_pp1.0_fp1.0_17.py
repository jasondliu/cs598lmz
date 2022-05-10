import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is the file descriptor of the file to be mapped.
# length is the number of bytes to map.
# flags is one of mmap.MAP_SHARED, mmap.MAP_PRIVATE, mmap.MAP_ANONYMOUS, or a
# combination of the flags defined in the mmap module.
# prot is one of mmap.PROT_READ, mmap.PROT_WRITE, or mmap.PROT_EXEC, or a
# combination of these.
# access is one of mmap.ACCESS_DEFAULT, mmap.ACCESS_COPY, mmap.ACCESS_READ,
# or mmap.ACCESS_WRITE.
# offset is the offset from the beginning of the file at which to start mapping
# (default is 0).

import os
import mmap

# Open the file for reading
f = open('lorem.txt', 'r')

# Create a mmap object

