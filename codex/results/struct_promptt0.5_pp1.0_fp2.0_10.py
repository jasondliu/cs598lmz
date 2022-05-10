import _struct
# Test _struct.Struct.pack_into()
import array
from test import support
from test.support import bigaddrspacetest

# This test is only relevant for 32-bit platforms.
@bigaddrspacetest
class StructOverflowTest(unittest.TestCase):
    def test_pack_into(self):
        # Issue #11913
        a = array.array('c', '\x00' * 1024)
        s = _struct.Struct('i')
        # This used to crash, now it raises an exception.
        self.assertRaises(OverflowError, s.pack_into, a, sys.maxsize, 1)


def test_main():
    support.run_unittest(StructOverflowTest)

if __name__ == "__main__":
    test_main()
