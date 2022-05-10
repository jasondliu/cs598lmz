import select
# Test select.select() with a timeout.
# This test is not very interesting on Mac OS X because select() doesn't
# support timeouts.
# XXX: This test is currently disabled because it fails on Windows.
# See issue #13642.
import sys
import time
import unittest
from test import support

if sys.platform == 'darwin':
    raise unittest.SkipTest('select.select() on Mac OS X does not support timeouts')
if sys.platform == 'win32':
    raise unittest.SkipTest('test_select.py is currently disabled on Windows')

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.read_fds = []
        self.write_fds = []
        self.error_fds = []

    def tearDown(self):
        for fd in self.read_fds:
            fd.close()
        for fd in self.write_fds:
            fd.close()
        for fd in self.error_fds:
            fd.close()

   
