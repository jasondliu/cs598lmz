import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# fileno is the file descriptor for the file being mapped (and should be open for reading or writing).

# length is the number of bytes to map (if zero, the maximum length of the file is used)

# flags is one of MAP_SHARED, MAP_PRIVATE, MAP_ANONYMOUS, or a bitwise OR of these values.

# prot is one of PROT_WRITE, PROT_READ, or a bitwise OR of these values.

# access is either mmap.ACCESS_DEFAULT or mmap.ACCESS_COPY.

# offset, if specified, is where in the file the mapping should start.

# mmap.mmap() returns a mmap object.

# mmap objects are like a file object, but the data is read directly from the operating system's virtual memory.

# mmap objects support the file protocol.
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset
