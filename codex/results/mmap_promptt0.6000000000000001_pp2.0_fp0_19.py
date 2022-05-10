import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])

# https://docs.python.org/3.7/library/mmap.html#mmap.mmap

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Map length bytes from the file specified by the file descriptor fileno, and return a mmap object. 
# If length is larger than the current size of the file, the file is extended to contain length bytes.
# If length is 0, the maximum length of the map will be the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).
# The flags argument specifies the nature of the mapping. MAP_SHARED creates a read-write mapping, so changes written to the mmap object will be visible to other processes that map this file, and changes made to the underlying file will be visible through the mmap object (depending on platform, on some systems, changes made to the file may or may not be immediately visible; see
