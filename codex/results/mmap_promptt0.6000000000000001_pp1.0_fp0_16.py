import mmap
# Test mmap.mmap
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map using the file descriptor fd. The size of
# the map is specified in length bytes. The optional flags argument
# defaults to mmap.MAP_SHARED. The optional prot argument defaults to
# mmap.PROT_WRITE | mmap.PROT_READ. The optional access argument
# defaults to mmap.ACCESS_DEFAULT. The optional offset argument
# defaults to 0.
#
# If length is 0, the maximum length of the map will be the current
# size of the file when mmap is called.
#
# If offset is specified and is not a multiple of the page size as
# returned by os.sysconf('SC_PAGE_SIZE'), then it is adjusted to the
# next page boundary. If length is not 0, length is also adjusted to
# the next page boundary. The offset must be a multiple of the page
# size on some systems, so you may need to round it down yourself if
# you don't want to
