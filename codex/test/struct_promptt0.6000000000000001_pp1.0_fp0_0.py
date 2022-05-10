import _struct
# Test _struct.Struct.


class StructTest(unittest.TestCase):
    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct(b"xyz", 42)

    def test_unpack_from(self):
        S = _struct.Struct(b"i")
        with self.assertRaises(TypeError):
            S.unpack_from()
        with self.assertRaises(TypeError):
            S.unpack_from(b"")
        with self.assertRaises(TypeError):
            S.unpack_from(b"", 42)
        with self.assertRaises(TypeError):
            S.unpack_from(b"", 42, 42)


if __name__ == "__main__":
    unittest.main()
