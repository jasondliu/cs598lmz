import mmap
# Test mmap.mmap()
#
# This test is not complete, but it does test the basic functionality.
#
# XXX To do:
# 1) Test use of mmap with a file opened in append mode.
# 2) Test use of PROT_EXEC.
# 3) Test use of MAP_PRIVATE and MAP_SHARED.
# 4) Test use of MAP_FIXED.
# 5) Test use of mmap with a file descriptor.
# 6) Test use of mmap with a buffer.
# 7) Test use of mmap with a negative length.
# 8) Test use of mmap with a length of 0.
# 9) Test use of mmap with a length of sys.maxint.
# 10) Test use of mmap with a file offset that is not a multiple of the
#     page size.
# 11) Test use of mmap with a file offset that is negative.
# 12) Test use of mmap with a file offset that is too large.
# 13) Test use of mmap with a file offset that is too large.
# 14) Test use of mmap with a file offset that is
