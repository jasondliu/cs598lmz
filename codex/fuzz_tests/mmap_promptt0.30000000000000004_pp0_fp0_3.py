import mmap
# Test mmap.mmap()
#
# This test is derived from the test case for mmap.mmap() in the Python
# library test suite, Lib/test/test_mmap.py.
#
# The test case is modified to use a temporary file, and to use a file
# size that is a multiple of the system page size.  The file is created
# with a known size, and the test case verifies that the size of the
# mmap object is the same as the size of the file.
#
# The test case also verifies that the mmap object can be used to write
# to the file, and that the file can be read back with the mmap object.

# Create a temporary file with a known size.

import tempfile

f = tempfile.TemporaryFile()

# Get the system page size.

import os

page_size = os.sysconf("SC_PAGE_SIZE")

# Create a temporary file that is a multiple of the system page size.

file_size = page_size * 10

f.seek(file_size - 1)
f.write(
