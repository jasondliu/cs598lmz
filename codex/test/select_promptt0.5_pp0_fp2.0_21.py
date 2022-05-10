import select
# Test select.select

# I'm not sure if this is the right way to test select.select.
# I'm not sure what the right way is.
#
# This test is not exhaustive.  It doesn't try all possible
# combinations of arguments.  It doesn't try all possible
# file objects.
#
# XXX Timeouts don't work on Windows with sockets.
# XXX Timeouts don't work on Solaris with pipes.
#
# XXX The test fails if stdin is a tty, because stdin is treated
# XXX differently from other files. 

import os, sys, time
from test_support import TestFailed, run_unittest

# Test the basic operation of select().
# Does it apply the right masks to the right file objects?

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.r, self.w = os.pipe()

    def tearDown(self):
        os.close(self.r)
        os.close(self.w)

