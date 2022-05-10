import mmap
# Test mmap.mmap()
#
# This is a test script for mmap.mmap()
#
# It tests the following:
#     - mmap.mmap()
#     - mmap.mmap().size()
#     - mmap.mmap().tell()
#     - mmap.mmap().seek()
#     - mmap.mmap().read()
#     - mmap.mmap().write()
#     - mmap.mmap().close()
#
# This test script was written by Bill Tutt. It is hereby placed in
# the public domain.

import os
import mmap
import string
import sys

def test_mmap(filename, size):
    # Create a file to mmap.
    fd = os.open(filename, os.O_RDWR | os.O_CREAT)
