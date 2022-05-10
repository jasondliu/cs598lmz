import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Returns an mmap object.

# fileno is the file descriptor returned by os.open() or os.pipe().

# length is the number of bytes to map.

# flags is one of the MAP_* constants (see below).

# prot is the desired memory protection for the mapping. It is one of PROT_* constants (see below).

# access is the desired access to the mapping. It is one of the ACCESS_* constants (see below).

# offset is the offset into the file.

# If you want to map an entire file, specify length as 0.

# If the file is smaller than the requested size, the entire file is mapped.

# If the file is larger than the requested size, only the portion up to length is mapped.

# If the file is larger than the requested size and length is 0, the entire file is mapped.

# If the file is empty, the entire file is mapped.

# If the file is empty and length is 0
