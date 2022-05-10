import _struct
# Test _struct.Struct with a format that doesn't fit into the size cache.
# This is a regression test for SF bug #1465990.
import sys
import unittest
import _testcapi

class StructTest(unittest.TestCase):
    def test_size(self):
        # This format has a size of 2**31 + 1, which doesn't fit into a
        # signed int.
        fmt = "P" * ((sys.maxsize + 1) // _testcapi.SIZEOF_VOID_P)
        self.assertRaises(ValueError, _struct.Struct, fmt)


def test_main():
    test.support.run_unittest(StructTest)

if __name__ == "__main__":
    test_main()
