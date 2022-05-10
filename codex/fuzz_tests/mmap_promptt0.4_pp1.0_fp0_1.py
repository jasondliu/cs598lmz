import mmap
# Test mmap.mmap.read
#
# This test is part of the mmap module test suite.
#
# The mmap module defines the following method:
#
# mmap.mmap.read(size)
#
# This method reads at most size bytes from the mmap'ed file.  If the
# file is smaller than size, the whole file is read.  The return value
# is a string containing the bytes read.  If the file was not opened
# in read mode, an exception is raised.
#
# This test verifies the correct operation of this method.

import unittest
import os

from test import test_support

# Create a file with some data.
filename = test_support.TESTFN
file = open(filename, "wb")
file.write("1234567890" * 1000)
file.close()

# Map the file, read it, and check the data.
file = open(filename, "r+b")
map = mmap.mmap(file.fileno(), 0)
data = map.read(100)
if data != "1234567890"
