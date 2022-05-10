import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is the file descriptor of the file to be mapped,
# length is the length of the mapping,
# flags is the bitwise OR of mmap.MAP_PRIVATE, mmap.MAP_SHARED, mmap.MAP_ANONYMOUS,
# prot is the bitwise OR of mmap.PROT_READ, mmap.PROT_WRITE, mmap.PROT_EXEC,
# access is the bitwise OR of mmap.ACCESS_READ, mmap.ACCESS_WRITE, mmap.ACCESS_COPY,
# offset is the offset in the file where the mapping starts.
#
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is the file descriptor of the file to be mapped,
# length is the length of the mapping,
# flags is the bitwise OR of mmap.MAP_PRIVATE,
