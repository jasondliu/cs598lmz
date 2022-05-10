import mmap
# Test mmap.mmap

# https://docs.python.org/3/library/mmap.html

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Open a file as a memory-mapped file.

# fileno is an integer file descriptor of the file to be memory-mapped.
# length is the number of bytes to map.
# flags is one of MAP_SHARED, MAP_PRIVATE, MAP_FIXED, MAP_ANONYMOUS, MAP_ANON
# prot is one of PROT_READ, PROT_WRITE, PROT_EXEC, PROT_NONE
# access is one of ACCESS_DEFAULT, ACCESS_READ, ACCESS_WRITE, ACCESS_COPY
# offset is the offset in the file at which to start mapping.
#
# The returned mmap object can be used as a context manager.
#
# If the underlying file is modified by another process,
# the changes are reflected in the mmap object’s contents.
#
# If the underlying file is truncated by another process,
