import mmap
# Test mmap.mmap()
#
# This test tries to mmap a file that doesn't exist.
#
# MMAP_FILE is a file that will be created by this test.
#
# This test is supposed to fail.
#
# This test was written by Andrew Johnson <ajohnson@redhat.com>
#

import os
import sys
import unittest
import test.support
import mmap

MMAP_FILE = test.support.TESTFN

