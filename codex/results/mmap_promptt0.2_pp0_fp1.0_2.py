import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map using the file descriptor fileno,
# and having the given access.
#
# The length argument specifies the number of bytes to map.
# The offset argument specifies the position within the file
# from which the bytes are to be mapped.
#
# The flags argument specifies the nature of the mapping.
#
# The prot argument specifies the desired memory protection of
# the mapping (one of PROT_READ, PROT_WRITE, or PROT_EXEC).
#
# The access argument specifies the desired access to the
# mapping (one of ACCESS_DEFAULT, ACCESS_READ, ACCESS_WRITE,
# or ACCESS_COPY).
#
# The returned object is a mmap object.
#
# The mmap object supports the following methods:
#
# mmap.close()
#
# Close the memory map. Further operations on the object will raise a ValueError.
#
# mmap.find(sub[, start[
