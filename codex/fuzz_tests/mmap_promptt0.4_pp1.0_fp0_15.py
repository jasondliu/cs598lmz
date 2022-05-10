import mmap
# Test mmap.mmap
#
# This module provides an interface to the Unix memory mapped file
# facilities.  It is an interface to the Unix system call mmap(2), and
# also to the msync(2) and munmap(2) calls.
#
# Memory mapped files are used for accessing small segments of large
# files on disk, without reading the entire file into memory.
#
# To create a memory map, use the mmap() function.  It takes three
# arguments: a file descriptor, a length, and flags.  The flags are
# described in the mmap(2) man page.
#
# The file descriptor fd must be opened in read/write mode, unless MAP_PRIVATE
# is given as a flag.  It is up to the user to open and close the file descriptor.
#
# The length argument specifies the number of bytes in the memory map.
#
# The flags argument is a bitwise-or of the constants described in the
# mmap(2) man page.
#
# The returned object is a mmap object.
#
# The mmap object behaves like a (read-only
