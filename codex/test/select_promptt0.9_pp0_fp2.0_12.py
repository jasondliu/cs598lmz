import select
# Test select.select() with objects that are not sockets.
import unittest
from test.support import verbose, TESTFN

if verbose:
    def debug(msg):
        print(msg)
else:
    def debug(msg):
        pass

#
# Test input/output behaviour of selectable objects.
#

class TestBase:
    """Base class with default behaviour common to all windows."""

    # Default behaviour of all objects is that they're blocking.
    should_block = True

    # True iff this file should allow a buffer (test_buffer).
    allows_buffer = False

    def setUp(self):
        self.filename = TESTFN

        # Buffer size to use in test_buffer.
        if self.allows_buffer:
            self.buffer_size = 4096

    def tearDown(self):
        support.unlink(self.filename)

    def test_blocking(self):
        # Should we block or not?
        debug('test_blocking: enter')
