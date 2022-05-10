import mmap
# Test mmap.mmap()
#
# This function is used to open a file as a memory-mapped object.
#
# It is similar to the Unix mmap() function.
#
# Syntax
#
# Following is the syntax for mmap.mmap() method −
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Parameters
#
#     fileno − This is the file descriptor for the file to be mapped.
#
#     length − This is the length of the mapping (number of bytes to map).
#
#     flags − This is one of the mmap.MAP_* constants describing the type of the mapping.
#
#     prot − This is the desired memory protection of the mapping.
#
#     access − This is the desired access to the mapping.
#
#     offset − This is the offset where the mapping starts (in bytes).
#
# Return Value
#
# This method returns the memory-mapped object.
#
# Example
#
# The following example shows the usage of mmap.mmap() method
