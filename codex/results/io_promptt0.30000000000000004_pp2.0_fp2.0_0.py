import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support
from test.support import _4G, _4GPlus1, bigmemtest

# A mixin for testing raw I/O
class BaseRawIOSharingTests:
    # This test is not designed to run on a system with a real raw
    # device, since it may clobber data.  It should only be run with
    # a RawIO implementation that emulates a raw device.

    def test_share_fd(self):
        # Test that a file descriptor can be shared between raw and
        # non-raw objects.
        f = open(support.TESTFN, "wb")
        try:
            f.write(b"spam")
            f.flush()
            fno = f.fileno()
            r = self.RawIO(fno)
            try:
                if r.read(4) != b"spam":
                    self.fail("read on raw file object failed")
                if f.read(4) != b"spam":
                    self.fail("
