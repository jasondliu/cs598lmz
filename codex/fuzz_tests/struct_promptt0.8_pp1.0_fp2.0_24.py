import _struct
# Test _struct.Struct.
import test.support

import copy
import sys
import weakref
from test import mapping_tests
try:
    import _testbuffer
except ImportError:
    _testbuffer = None

if sys.byteorder != "little":
    print("This test only works with little endian systems.", file=sys.stderr)
    sys.exit(0)

### Sized, Mapping & MutableMapping Interfaces ################################


class BaseTest:
    def setUp(self):
        self.format = 'hhl'
        self.s = _struct.Struct(self.format)
        self.size = self.s.size
        self.packed1 = b'\x01\x02\x00\x00\x00\x00\x00\x00'
        self.packed2 = b'\x02\x01\x00\x00\x00\x00\x00\x00'
        self.unpacked = (0x0201, 0x0003, 0x00000405)

    def test_unpack(self
