import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT, offset=0)
#
# fileno: The file descriptor of the file to map.
# length: The length of the map.
# flags: The flags to pass to the kernel.
# prot: The protection to apply to the memory.
# access: The access to the memory.
# offset: The offset into the file to start the map.
#
# The flags can be one of the following:
#
# MAP_SHARED: Changes are shared.
# MAP_PRIVATE: Changes are private.
# MAP_ANONYMOUS: No file is associated with the mapping.
# MAP_ANON: Same as MAP_ANONYMOUS.
# MAP_DENYWRITE: Forbid write access to the mapped region.
# MAP_EXECUTABLE: Forbid execution of code in the mapped region.
# MAP_FILE: The mapping is backed by a file.
# MAP_FIXED: The mapping
