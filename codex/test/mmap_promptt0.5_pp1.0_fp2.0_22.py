import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE, access=ACCESS_DEFAULT, offset=0)

# mmap() creates a new mapping in the virtual address space of the calling process. The starting address for the new mapping is specified in addr. The length argument specifies the length of the mapping.
# The flags argument determines whether updates to the mapping are visible to other processes mapping the same region, and whether updates are carried through to the underlying file. It is either MAP_SHARED or MAP_PRIVATE, optionally or'ed with MAP_FIXED. If MAP_FIXED is specified, then the addr argument must be aligned on a page boundary. This flag is available on some Unix implementations.
# The prot argument describes the desired memory protection of the mapping (either PROT_READ, PROT_WRITE, or both). The access argument determines whether pages may be read from, written to, or executed, and should be either ACCESS_DEFAULT, ACCESS_READ, ACCESS_WRITE, or ACCESS_COPY.
# The offset argument specifies the file offset where the mapping
