import _struct
# Test _struct.Struct class.

import test.support, unittest

import _testcapi

class StructTestCase(unittest.TestCase):

    def test_pack_int(self):
        packed = _struct.pack("i", 2)
        self.assertEqual(packed, b'\x02\x00\x00\x00')

        # Issue 9843
        packed = _struct.pack("i", -2)
        self.assertEqual(packed, b'\xfe\xff\xff\xff')

        # Issue 10131
        packed = _struct.pack("i", 128)
        self.assertEqual(packed, b'\x80\x00\x00\x00')

    @test.support.bigmemtest(size=_testcapi.INT_MAX + 1, memuse=1)
    def test_pack_uint(self, size):
        _struct.pack("I", size)

    @unittest.skipUnless(hasattr(_testcapi, "LARGE_STRUCT_SIZE"),
                         'requires C API for large struct
