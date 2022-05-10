import mmap
# Test mmap.mmap()

# map = mmap.mmap(fd, length, access=mmap.ACCESS_WRITE)
# map = mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# The fileno and length arguments specify the portion of the file to be mapped.

# The flags argument specifies the nature of the mapping.

# The prot argument specifies the desired memory protection of the mapping (this is ignored on some platforms).

# The access argument specifies the desired access to the data.

# The offset argument specifies the offset within the file from which the mapping starts (this is ignored on some platforms).

# The size of the mapped view can be obtained by calling:

# map.size()
# map.tell()

# To unmap the mapped region, use:

# map.close()


# The map object has the following methods:

# map.read(n)
# map.readline()
# map.read_byte()
# map.readline()
# map.readlines()
# map.seek(offset, whence=
