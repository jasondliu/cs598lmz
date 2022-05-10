import mmap
# Test mmap.mmap()
# Test mmap.mmap.__new__()

import os, stat

try:
    from test.support import TESTFN, run_unittest
except ImportError:
    from test.test_support import TESTFN, run_unittest

# For testing seek() and tell()
TEST_DATA = b'abcdefghijklmnop'*4


class MmapTests(unittest.TestCase):
    def setUp(self):
        # Create a file to be mmap'ed.
        with open(TESTFN, 'wb') as f:
            f.write(TEST_DATA)

    def tearDown(self):
        os.unlink(TESTFN)

    def test_access(self):
        # Test mmap.mmap() access modes

        # Open the file
        f = open(TESTFN, 'r+b')
        # Create an mmap object
        m = mmap.mmap(f.fileno(), 0)
        # Test read
