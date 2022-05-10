import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Return an mmap object.
#
# The fileno and length arguments specify the length of the mapping.
# The flags argument specifies the nature of the mapping.
# The prot argument specifies the page protection of the mapping.
# The access argument specifies the access to the mapping.
# The offset argument specifies the offset from the beginning of the file.
#
# The flags argument is a bitwise OR of the following flags:
#
# mmap.MAP_SHARED
# Share this mapping.
#
# mmap.MAP_PRIVATE
# Create a private copy-on-write mapping.
#
# mmap.MAP_FIXED
# Interpret addr exactly.
#
# The prot argument is a bitwise OR of the following flags:
#
# mmap.PROT_EXEC
# Pages may be executed.
#
# mmap.PROT_READ
# Pages may be read.
#
# mmap.PROT_WRITE
# Pages may
