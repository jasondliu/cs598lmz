import mmap
# Test mmap.mmap()
#
# This test is derived from test_mmap.py.
#
# The mmap module defines the following functions:
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Create a new memory map.  The fileno and length arguments specify
# the underlying file.  The optional flags argument specifies how the
# file is to be opened: os.O_RDONLY, os.O_WRONLY, or os.O_RDWR.  If
# not specified, os.O_RDWR is used.
#
# The optional prot argument specifies the access permissions of the
# new memory map.  It defaults to PROT_WRITE.
#
# The optional access argument specifies the initial access to the
# memory.  It defaults to ACCESS_DEFAULT.
#
# The optional offset argument specifies the offset from the beginning
# of the file at which to start the mapping.  It defaults to 0.
#
# The return value is a mmap object.
#
# mmap.mmap(length[, flags
