import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# Map length bytes from the file specified by the file descriptor fileno, and
# return a mmap object. If length is larger than the current size of the file,
# the file is extended to contain length bytes. If length is 0, the maximum
# length of the map is the current size of the file, except that if the file is
# empty Windows raises an exception (you cannot create an empty mapping on
# Windows).

# The flags argument specifies the nature of the mapping. MAP_SHARED creates a
# shareable mapping, so that the file’s contents may be seen by other processes
# that map the same file; MAP_PRIVATE creates a private copy-on-write mapping,
# so that changes to the contents of the mmap object will be private to this
# process. On Windows, MAP_SHARED and MAP_PRIVATE are the only allowed values
# for flags.

# The prot argument specifies the desired memory protection of the mapping
# (either PROT_READ or
