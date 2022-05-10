import _struct
# Test _struct.Struct
import collections
import math
import random
import test.support
import unittest
import sys
try:
    import _testbuffer
except ImportError:
    _testbuffer = None
try:
    import array
except ImportError:
    array = None
try:
    import mmap
except ImportError:
    mmap = None
try:
    import _testcapi
except ImportError:
    _testcapi = None
def isaligned(s, alignment=sizeof(c_void_p)):
    adr = addressof(s)
    return (adr & (alignment - 1)) == 0
class StructTestCase(unittest.TestCase):
    align = None
    format = None
    expected_size = None
    expected_alignment = None

    def setUp(self):
        self._keepalive = []
        fmt = self.format
        if hasattr(self, 'extra'):
            fmt = fmt + self.extra
        if hasattr(self, 'prefix'):
            fmt = self.prefix + fmt
        self.s
