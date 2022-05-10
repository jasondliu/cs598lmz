import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is the file descriptor of the file to be mapped.
# length is the number of bytes to map.
# flags is one of mmap.MAP_PRIVATE, mmap.MAP_SHARED, mmap.MAP_ANONYMOUS,
# mmap.MAP_ANON, mmap.MAP_HASSEMAPHORE, mmap.MAP_NOCACHE, mmap.MAP_NOSYNC,
# mmap.MAP_SCAN, mmap.MAP_NORESERVE, mmap.MAP_ALIGN, mmap.MAP_FIXED,
# mmap.MAP_RENAME, mmap.MAP_RESERVED0080, mmap.MAP_RESERVED0100,
# mmap.MAP_RESERVED0200, mmap.MAP_RESERVED0400, mmap.MAP_RESERVED0800,
# mmap.MAP_RESERVED1000, mmap
