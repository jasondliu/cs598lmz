import _struct
# Test _struct.Struct

Struct = _struct.Struct

class TestStruct:

    def __init__(self):
        self.s = Struct(">hhl")

    def test_unpack_from(self):
        b = b"\x01\x02\x00\x03\x00\x00\x00\x04"
        f = io.BytesIO(b)

        self.assertEqual(self.s.unpack_from(f), (258, 772, 67305985))

class TestStructErrors(unittest.TestCase):

    def test_struct_error(self):
        self.assertIsInstance(Struct.error, TypeError)

if __name__ == "__main__":
    unittest.main()
