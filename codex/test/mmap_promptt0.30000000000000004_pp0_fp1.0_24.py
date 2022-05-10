import mmap
# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html
#
# This is a simple example of how to use mmap.mmap() to map a file into memory.
#
# The mmap module defines the following class:
#
# class mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#     Create a memory-map to an existing file.
#
# The file must be opened in a way that supports mmap (see mmap()).
#
# The length argument specifies the length of the mapping (which must be less
# than or equal to the current size of the file).
#
# The flags argument specifies the nature of the mapping. MAP_SHARED means that
# the mapping is visible to other processes mapping the same region, and that
# changes are visible in the underlying object. MAP_PRIVATE means that changes
# are private to this process, and are not visible to other processes mapping
# the same region.
#
# The prot argument specifies the desired memory protection of the mapping
# (this is ignored on Windows).
