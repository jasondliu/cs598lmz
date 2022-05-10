import mmap
# Test mmap.mmap()
#
# mmap.mmap(...)
#     mmap(fileno, length[, access[, offset]]) -> mmap object
#
# Create a memory-map to an object in a file.
# The first argument is an integer or long integer giving the file
# descriptor of the file to be mapped; the second argument is the length
# of the mapping.
#
# If the optional third argument is mmap.ACCESS_READ, the mapping
# accesses the file in read-only mode; if it is mmap.ACCESS_WRITE, the
# mapping accesses the file in write-through mode; if it is
# mmap.ACCESS_COPY, the mapping accesses the file in copy-on-write mode.
# If the file is opened in append mode, only mmap.ACCESS_WRITE is allowed.
#
# The optional fourth argument is the offset, in bytes, into the file of
# the first byte in the memory-mapped region.  If this argument is not
# specified, the file offset is used.
#
# If the file is opened in append
