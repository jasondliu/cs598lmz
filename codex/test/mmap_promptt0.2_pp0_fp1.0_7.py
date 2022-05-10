import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map using the file specified by the file handle fileno,
# and having at least length bytes available, starting at offset.  The entire
# file is mapped by default.  flags and prot arguments specify the nature of
# the mapping.  access is ignored on Windows.
#
# The flags argument specifies the nature of the mapping.  MAP_SHARED
# creates a mapping that's shared with all other processes mapping the same
# file; modifications to the mapping are visible to all other processes that
# map this file, and are carried through to the underlying file.  On the other
# hand, MAP_PRIVATE creates a private copy-on-write mapping, so changes to the
# contents of the mmap object will be private to this process, and MAP_ANONYMOUS
# creates a mapping that isn't backed by any file; modifications are never
# written through to the underlying file.
#
# The prot argument specifies the access allowed to the mapping.  It is either

