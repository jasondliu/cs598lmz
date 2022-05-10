import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT, offset=0)

# fileno:
#   The file descriptor used to create the mmap object.
#   The file must be opened with the os.O_RDWR flag.
#   The file must be opened in binary mode, not text mode.
#
# length:
#   The length of the mapping (number of bytes to map).
#
# flags:
#   The flags argument specifies the nature of the mapping.
#   It is a bitwise OR of one or more of the following constants:
#
#   mmap.MAP_SHARED
#     Share this mapping.
#     When two or more processes share a mapping, they see a single,
#     coherent view of the file.
#     When one process updates the mapping, the other processes see the changes.
#
#   mmap.MAP_PRIVATE
#     Create a private copy-on-write mapping.
#     Updates to the
