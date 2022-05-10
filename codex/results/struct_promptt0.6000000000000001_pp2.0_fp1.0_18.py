import _struct
# Test _struct.Struct
from struct import Struct

from test import support
from test.support import bigaddrspacetest

# Helper to test _struct.Struct
def structhelper(code, format, values, expected):
    s = Struct(format)
    buf = s.pack(*values)
    result = s.unpack(buf)
    if result != expected:
        print(code, format, values, result, expected)

class StructTestCase(unittest.TestCase):
    def test_bool(self):
        # Issue #1714: pack and unpack booleans
        for format in '?', 'B', 'b', 'H', 'h', 'I', 'i', 'Q', 'q', 'f', 'd':
            structhelper(format, format, (True,), (1,))
            structhelper(format, format, (False,), (0,))

    def test_large_long_long(self):
        # Issue #2930: pack 64 bit ints even on 32 bit platforms
        for format, value in [('q', 2**31-1
