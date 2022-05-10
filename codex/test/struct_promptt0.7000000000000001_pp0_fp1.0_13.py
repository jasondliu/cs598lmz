import _struct
# Test _struct.Struct
import test.support
from test.support import precisionbigmemtest, bigaddrspacetest
import unittest
import sys

# We used to test all native formats, but that was excessive.  There
# are really just two cases: standard size and standard size + 1 for
# 64-bit systems.  Note that we can't test all formats if longs are
# bigger than 8 bytes because there's no way to stuff 9 bytes into a
# long long.
formats = 'xcbhHiIlLfd'
if sys.maxsize > (1 << 32):
    formats += 'Qq'

class StructTest(unittest.TestCase):

    def test_unpack(self):
        # Test struct.unpack().
        for format in formats:
            s = _struct.Struct(format)
            size = s.size
            for n in (0, 1, 100):
                data = bytes(n*size)
                self.assertEqual(s.unpack(data), n*(tuple([0, ]),))
