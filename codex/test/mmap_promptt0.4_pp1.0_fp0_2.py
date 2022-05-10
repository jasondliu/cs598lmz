import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT, offset=0)
#
# fileno: The file descriptor of the file to map.
# length: The size of the mapping.
# flags: The type of the mapping.
# prot: The protection of the mapping.
# access: The access to the file.
# offset: The offset in the file.
#
# The flags argument can be one of the following:
#
# MAP_SHARED: The mapping is shared with other processes.
# MAP_PRIVATE: The mapping is private to the current process.
#
# The prot argument can be one of the following:
#
# PROT_READ: The mapping is readable.
# PROT_WRITE: The mapping is writable.
# PROT_EXEC: The mapping is executable.
#
# The access argument can be one of the following:
#
# ACCESS_DEFAULT: The default access is given to the file.
# ACCESS_C
