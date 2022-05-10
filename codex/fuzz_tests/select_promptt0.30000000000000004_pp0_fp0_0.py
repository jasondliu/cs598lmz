import select
# Test select.select()
#

#
# Test select.select()
#

import select
import os
import sys
import time
import unittest

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.r, self.w = os.pipe()

    def tearDown(self):
        os.close(self.r)
        os.close(self.w)

    def test_select(self):
        # test that select.select() works with pipes
        #
        # We test by writing some data to a pipe and then ensure
        # that select returns that the pipe is ready to read.
        #
        data = "1"
        os.write(self.w, data)
        r, w, x = select.select([self.r], [], [], 1)
        self.assertTrue(r == [self.r])

    def test_select_timeout(self):
        # test that select.select() timeout works
        #
        # We test by writing some data to a pipe and then ensure
        # that select returns that
