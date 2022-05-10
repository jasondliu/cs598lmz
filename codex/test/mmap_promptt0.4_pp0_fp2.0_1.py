import mmap
# Test mmap.mmap(0,1)
# It returns a zero-length mmap object.
# It is not a valid file descriptor, but it is a valid mmap object.
# It can be used to test if mmap is available on the system.
# This test is used in the Python mmap module.
#
# Written by:
#   Fred L. Drake, Jr.
#   fdrake@acm.org
#   http://www.python.org/~fdrake

import mmap

