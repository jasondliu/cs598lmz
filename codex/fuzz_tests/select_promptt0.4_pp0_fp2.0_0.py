import select
# Test select.select() with a large number of file descriptors.
#
# This test is not portable, because it depends on the implementation
# of select() and the underlying operating system.
#
# Written by Martin v. Löwis <loewis@informatik.hu-berlin.de>
#

import os
import select
import sys
import time
import unittest

from test.support import run_unittest, TESTFN, unlink

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.readable = []
        self.writable = []
        self.errorable = []
        self.timeout = 60.0

    def tearDown(self):
        for f in self.readable + self.writable + self.errorable:
            f.close()

    def test_select(self):
        # create a bunch of pipes
        for i in range(16):
            r, w = os.pipe()
            self.readable.append(os.fdopen(r, "rb", 0))
            self.writable.append
