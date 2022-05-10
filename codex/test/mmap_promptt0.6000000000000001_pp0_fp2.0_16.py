import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, access[, offset]])
# Open file and create a memory-map to its contents.

# fileno is an integer file descriptor of the file to be memory-mapped.

# length is the number of bytes to map, or mmap.MAP_SIZE which maps the whole file.

# access is one of mmap.ACCESS_READ, mmap.ACCESS_WRITE, mmap.ACCESS_COPY, optionally ORed with mmap.ACCESS_DEFAULT.

# offset is the file offset where the mapping starts.

# mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# Open a named shared memory object and create a memory-map to it.

# tagname is the name of the shared memory object.

# The remaining arguments have the same meaning as for mmap().

# mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# Open an existing named shared memory object and create a memory-map to it.

