import mmap
# Test mmap.mmap()
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   This module defines the following functions:
#
#   mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]]) -> mmap object
#
#   Create a new memory-map to an existing file.  The file must be opened with
#   the os.O_RDWR (read/write) flag.
#
#   The optional flags argument has the same interpretation as the flags
#   argument to the built-in open() function.
#
#   The optional prot argument has the same interpretation as the prot argument
#   to the mmap.mmap() function.  The default is mmap.PROT_WRITE.
#
#   The optional access argument has the same interpretation as the access
#   argument to the mmap.mmap() function.  The default is mmap.ACCESS_WRITE.
#
#   The optional offset argument is the offset (in bytes) into the file where
#   the mapping should begin.  The default is 0 (the beginning of the file).

