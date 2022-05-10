import _struct
# Test _struct.Struct
class BigEndianTest(unittest.TestCase):
    def test_pack(self):
        for typecode in _struct.STRUCT_UNPACK:
            packing = _struct.Struct(">%c" % typecode).pack
            self.assertRaises(TypeError, packing)
            self.assertRaises(TypeError, packing, None)
            self.assertRaises(TypeError, packing, 1, 2)

    def test_unpack(self):
        for typecode in _struct.STRUCT_UNPACK:
            unpacking = _struct.Struct(">%c" % typecode).unpack
            self.assertRaises(TypeError, unpacking)
            self.assertRaises(TypeError, unpacking, None)
            self.assertRaises(TypeError, unpacking, 1, 2)
            self.assertEqual(unpacking(""), (0,))
            self.assertRaises(TypeError, unpacking, "", None)
            self.assertRaises(TypeError, unpacking, "", 1, 2)

