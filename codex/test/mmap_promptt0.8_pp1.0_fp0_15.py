import mmap
# Test mmap.mmap.resize
#
# The issue is that Unix can't resize a file beyond the EOF mark.  This
# behavior is undocumented in the Python manual, but tested in the test
# suite.  Windows can resize a file beyond the EOF mark.  The previous
# implementation of mmap.mmap.resize, which was written before support
# for Windows, would attempt to resize the file.  This fails on Unix,
# and causes a segfault on Windows.
#
# The "correct" solution would be to add a new OS-specific mmap module
# to support Windows, which would have an implementation of resize that
# would handle the differences between it and Unix.  However, as of
# Python 2.2.2, this was not done.  Instead, the "new" implementation
# of resize simply does not resize the file.  This behavior is
# consistent with the test suite, and is not a regression for any
# platform.
#
# This test case is a regression test for the new implementation of
# resize.  It is based on the file test_mmap.py, which is shipped
# with Python
