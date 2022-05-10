import select
# Test select.select() with a file descriptor that is not in the right range
# (0..FD_SETSIZE).  This test is only meaningful on platforms where select()
# doesn't accept file descriptors above FD_SETSIZE.

import select
import unittest

class SelectTestCase(unittest.TestCase):
    def test_select_fd_out_of_range(self):
        # Issue #10077: select.select() should raise an error if fd is out of
        # range.
        self.assertRaises(ValueError, select.select, [], [], [], 0,
                          FD_SETSIZE + 1)

if __name__ == "__main__":
    unittest.main()
