import mmap
# Test mmap.mmap(0, 1)
#
# This is a test for SF bug #1254336: mmap.mmap(0, 1) failed to raise an exception
#
# http://www.python.org/sf/1254336

import os
import unittest
from test import test_support
import mmap

class MmapTests(unittest.TestCase):
    def test_anonymous(self):
        # can't write to anonymous mmap'ed file
        try:
            mmap.mmap(-1, 1)
        except ValueError:
            pass
        else:
            self.fail("mmap(-1, 1) didn't raise ValueError")

def test_main():
    test_support.run_unittest(MmapTests)


if __name__ == "__main__":
    test_main()
