import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Create a new memory map using the file descriptor fileno, the size length, and the optional flags which can be one of the following:
# mmap.MAP_SHARED
# Share this map with all other processes that map this file. Changes to the file and the mappings are visible to all other processes mapping the file.
# mmap.MAP_PRIVATE
# Create a private copy-on-write mapping. Changes to the mapping are private to this process, and are not visible to other processes mapping the same file. The file may not actually be updated until msync() or munmap() is called.
# mmap.MAP_FIXED
# Don't interpret addr as a hint: place the mapping at exactly that address. addr must be a multiple of the page size. If the memory region specified by addr and len overlaps pages of any existing mapping(s), then the overlapped part of the existing mapping(s) will be discarded. If the specified address cannot be used, mmap() will fail.
# If flags is given,
