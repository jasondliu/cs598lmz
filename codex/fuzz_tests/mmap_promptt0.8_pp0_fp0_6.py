import mmap
# Test mmap.mmap(-1, 100)

# When running our tests on Linux, we were sometimes receiving errors
# like this:
#
#   Bad file descriptor for mmap.mmap(-1, 4096)
#
# and eventually traced it down to this bug:
#
#   http://bugs.python.org/issue13511
#
# So, this test verifies that mmap.mmap(-1, 100) works as expected.
#

from mmap import mmap, ACCESS_READ, MAP_SHARED
import os
import unittest

class TestBadFD(unittest.TestCase):
    """
    Try to create an mmap with an fd that's already closed.
    """
    def test_mmap_with_bad_fd(self):
        _, filename = tempfile.mkstemp()
        with open(filename, "w+") as fp:
            fp.write("test data")
            fm2 = mmap(fp.fileno(), 100, access=ACCESS_READ)
        os.close(fp.fileno())
        f
