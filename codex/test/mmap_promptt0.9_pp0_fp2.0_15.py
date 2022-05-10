import mmap
# Test mmap.mmap function
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#   Create a new memory map from an existing file.  The file must "
#   be open for reading or writing.  The length argument specifies the
#   number of bytes to map.
#
#   If the length is larger than the current size of the file, only
#   the part within the current file size is mapped (the file size
#   may change during the life of the map).
#
#   If the length is 0, the maximum length of the map will be the
#   current size of the file, except if the file is empty, in which
#   case it will be zero.  
#
#   The offset specifies the offset within the file from which
#   the bytes should be read.
# The parameters fileno, length, prot, access, flags are the same as
# used in the Windows CreateFileMapping function.


dfile = open(r'z:\tmp\mac-cisco-nexus-old_os.rst.txt')
