import mmap
# Test mmap.mmap
#
# This is a test of the mmap module.
#
# This test is a bit tricky because mmap.mmap objects are not
# garbage-collected.  If you don't close them explicitly, they will
# be closed when the process exits, but that's not guaranteed to be
# before the garbage collector runs.  So, we need to keep track of
# all mmap objects we create and close them explicitly.
#
# We also need to keep track of all temporary files we create and
# delete them explicitly.
#
# The test is also tricky because we need to create a temporary file
# of a specific size, and we can't just seek to the end of the file
# and write a newline because that would change the semantics on
# MS-Windows.  So, we write a temporary file of a specific size using
# a separate program.

import os
import sys
import unittest
import mmap
import tempfile

from test import test_support

# Test the mmap module

# Test the constants
PAGESIZE = mmap.PAGESIZE

# Test the functions

