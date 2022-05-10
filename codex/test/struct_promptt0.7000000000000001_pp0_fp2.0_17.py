import _struct
# Test _struct.Struct
Struct = _struct.Struct

class TestStruct(unittest.TestCase):

    def test_wrong_format(self):
        # illegal format
        self.assertRaises(struct.error, Struct, "")
        self.assertRaises(struct.error, Struct, "abc")
        # known format, wrong size
        self.assertRaises(struct.error, Struct, "b")
        self.assertRaises(struct.error, Struct, "h")
        self.assertRaises(struct.error, Struct, "i")
        self.assertRaises(struct.error, Struct, "l")
        self.assertRaises(struct.error, Struct, "q")
        self.assertRaises(struct.error, Struct, "f")
        self.assertRaises(struct.error, Struct, "d")

    def test_pack(self):
        # known format, correct size, native byte order
        fmt = 'P'
        for i in range(len(self.some_floats)):
            p = Struct(fmt)
