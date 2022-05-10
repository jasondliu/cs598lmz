import mmap
# Test mmap.mmap()
#
# This test should be run with the program 'mmaptest.c'.
#
# mmaptest.c should be compiled with the command:
#
#    gcc -o mmaptest mmaptest.c
#
# mmaptest.c is a simple program that creates a file and writes the
# string "hello world" to it.  It then mmaps the file and verifies
# that the string was written correctly.  It then unmaps the file and
# exits.
#
# This test runs mmaptest.c and checks that it exits with a status of 0.
#
# The following functions are tested:
#    mmap.mmap()       map a file into memory

import os
import sys
import unittest
from test import support

# Skip this test if the OS doesn't support mmap.
try:
    mmap.mmap(-1, 1)
except (EnvironmentError, ValueError):
    raise unittest.SkipTest("mmap not supported by this system")

# Skip this test if the OS doesn't support anonymous mmap.
try:

