import mmap
# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT)
# fileno = file descriptor
# length = size of memory mapped to this FD
# flags = sharing mode (MAP_PRIVATE or MAP_SHARED)
# prot = Protection Visibility
#     PROT_READ = readable
#     PROT_WRITE = writable
#     PROT_NONE = inaccessible
# access = how you want to access this file
#     ACCESS_DEFAULT = read and write
#     ACCESS_COPY = copy on write (not useful)
#     ACCESS_READ = read only access
#     ACCESS_WRITE = write only access
#
#
# mmap.close() writes any changes to file, flushes and closes
#
# mmap.resize() resizes the map
#
# mmap.seek(offset[, where])
# offset can be negative to go backwards
# where = 0 start of map, 1 current position, 2 end of map
#
# mmap.tell() returns current
