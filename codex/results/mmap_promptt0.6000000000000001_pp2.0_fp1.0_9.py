import mmap
# Test mmap.mmap()

# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# Map length bytes from the file specified by the file descriptor fileno, 
# and create a mmap object. 
# The flags argument specifies the nature of the mapping. MAP_PRIVATE creates a private copy-on-write mapping, 
# so changes to the contents of the mmap object will be private to this process, 
# and MAP_SHARED creates a mapping that’s shared with all other processes mapping the same areas of the file. 
# The default value is MAP_SHARED.

# The prot argument specifies the access protections of the mapping. 
# This is either PROT_NONE or the bitwise OR of one or more of the other flags PROT_READ, PROT_WRITE, and PROT_EXEC. 
# The default value is PROT_READ. 
# If the file being mapped is empty, the resulting mmap object will contain zero bytes of the specified length. 
# If the file is extended, the contents of the mmap object will reflect those changes. 
