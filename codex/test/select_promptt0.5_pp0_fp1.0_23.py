import select
# Test select.select with a bad file descriptor.
from test import support
import unittest
from unittest import mock
import os
import errno

class SelectBadFdTests(unittest.TestCase):

    def test_select_bad_fd(self):
        fd = os.open(os.devnull, os.O_RDONLY)
        try:
            os.close(fd)
            self.assertRaises(OSError, select.select, [fd], [], [])
            self.assertRaises(OSError, select.select, [], [fd], [])
            self.assertRaises(OSError, select.select, [], [], [fd])
        finally:
            os.close(fd)

    @unittest.skipUnless(hasattr(os, 'dup'), 'test needs os.dup()')
    def test_select_closed_dup_fd(self):
        fd = os.open(os.devnull, os.O_RDONLY)
