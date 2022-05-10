import mmap
# Test mmap.mmap()
#
# This test is a bit different from the others.  It is not a test of
# the mmap module, but rather a test of the mmap.mmap() function.
#
# The mmap.mmap() function is used to create a memory-mapped file.
# This is a very useful feature, but it is not available on all
# platforms.  This test checks to see if mmap.mmap() is available on
# the current platform.  If it is, the test passes.  If it is not, the
# test is skipped.
#
# This test is not run by default.  To run it, use the -u mmap option.
#
# This test is not included in the standard test suite because it is
# not a test of the mmap module.  It is a test of the mmap.mmap()
# function.  If mmap.mmap() is not available, the mmap module is
# useless.  This test is here to make sure that the mmap module is not
# installed on platforms where mmap.mmap() is not available.

import
