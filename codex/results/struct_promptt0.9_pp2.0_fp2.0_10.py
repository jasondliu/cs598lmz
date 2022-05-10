import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):

    @unittest.skip("XXX re-enable this once we write a nice public API for structs")
    def test_struct_compat(self):
        # Test compatibility between CPython builtin struct and _struct.Struct
        s = _struct.Struct(">I")
        self.assertEqual(s.calcsize(122), 4)
        self.assertEqual(s.pack(122), b"\x00\x00\x00\x7a")
        self.assertEqual(s.unpack(b"\x00\x00\x00\x7a")[0], 122)
        self.assertEqual(s.unpack_from(bytearray(b"\x00\x00\x00\x7a"), 0)[0], 122)


if __name__ == "__main__":
    unittest.main()
