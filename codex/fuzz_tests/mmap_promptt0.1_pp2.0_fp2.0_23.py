import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map using the file specified by the file handle fileno,
# and having at least length bytes available, starting at offset.
#
# The flags argument specifies the nature of the mapping. MAP_SHARED creates a
# mapping that's shared with all other processes mapping the same areas of the
# file (or device). MAP_PRIVATE creates a private copy-on-write mapping, so
# changes to the contents of the mmap object will be private to this process,
# and MAP_ANONYMOUS creates a mapping that isn't backed by any file;
# modifications to the contents of the mmap object will never be written
# through to the underlying file.
#
# The prot argument specifies the desired memory protection of the mapping
# (this is ignored on Windows). It can be PROT_WRITE to enable writes to the
# memory region, and PROT_READ to enable reads.
#
# The access argument specifies the desired access to the mapping. It can be
# ACC
