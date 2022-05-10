import io
# Test io.RawIOBase forwarding
# https://docs.python.org/3/library/stdtypes.html#io.RawIOBase
#
# NOTE: This test case only tests the end-of-file case. We're unable to test
#       other cases because we don't have any other real raw I/O class to
#       instantiate.
import unittest
from test import support
from test.support import CapturingNullDevice
try:
    import _pyio
except ImportError:
    _pyio = None
RAW_IO_METHODS = set([attrib for attrib in dir(_pyio.BufferedIOBase)
      if not attrib.startswith('__')])


class EnhancedRawIOBase(io.RawIOBase):
    """A RawIOBase subclass that supports immediate re-reads and checksums."""

    def __init__(self, data, checksum=0):
        self.checksum = checksum
        self.data = data
        self.index = 0

    def readinto(self, b):
        if self.index >= len(self.data):
            return None

