import mmap
# Test mmap.mmap
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# fileno is an integer file descriptor of the file to be mapped.
# length is the number of bytes to map.
# flags is one of mmap.MAP_PRIVATE, mmap.MAP_SHARED, mmap.MAP_ANONYMOUS, or mmap.MAP_ANON.
# prot is one of mmap.PROT_EXEC, mmap.PROT_READ, mmap.PROT_WRITE, or mmap.PROT_NONE.
# access is either mmap.ACCESS_DEFAULT, mmap.ACCESS_READ, or mmap.ACCESS_WRITE.
# offset is the offset in the file to start the mapping.

# mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# tagname is the name of the shared memory block.
# access is either mmap.
