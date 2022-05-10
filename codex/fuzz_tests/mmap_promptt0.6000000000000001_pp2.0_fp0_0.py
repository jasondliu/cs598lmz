import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# fileno – This is the integer file descriptor of the file to be mapped.
# length – This is the number of bytes to map.
# flags – This is the optional flag which decides whether changes made to the memory map are visible to other processes mapping the same region, and whether updates are carried through to the underlying file.
# prot – This is the access protection of the map as either PROT_NONE or the bitwise OR of the access flags.
# access – This is the access policy. It can be either MAP_PRIVATE or MAP_SHARED.
# offset – This is the offset position within the file where the mapping is to begin.
#
# mmap.MAP_SHARED
# mmap.MAP_PRIVATE
# mmap.PROT_READ
# mmap.PROT_WRITE
# mmap.PROT_EXEC
# mmap.PROT_NONE
# mmap.ACCESS_READ
# mmap.ACCESS_WRITE
# mmap
