import _struct
# Test _struct.Struct on non-standard formats.
import _testcapi
from _testcapi import INT_MAX, INT_MIN
from test import support

class StructTest(unittest.TestCase):
    def test_nonstandard(self):
        _testcapi.check_nonstandard_fmt(self, 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
        _testcapi.check_nonstandard_fmt(self, 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
        _testcapi.check_nonstandard_fmt(self, 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
