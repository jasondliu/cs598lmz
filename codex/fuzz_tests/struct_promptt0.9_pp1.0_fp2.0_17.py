import _struct
# Test _struct.Struct("i").pack_into, ensure that's working
class TestPackInto(unittest.TestCase):
    def test_basic(self):
        fmt = _struct.Struct("i")
        buf = bytearray(range(5))
        fmt.pack_into(buf, 1, 1)
        self.assertEqual(buf, [0, 0, 0, 1, 4])
# Test _struct.Struct("BH").pack_into, ensure that's working
class TestPackInto_UBH(unittest.TestCase):
    def test_basic(self):
        fmt = _struct.Struct("BH")
        buf = bytearray(range(5))
        fmt.pack_into(buf, 1, 2, 1)
        self.assertEqual(buf, [0, 2, 0, 1, 4])
class TestUnpackFrom(unittest.TestCase):
    def test_basic(self):
        fmt = _struct.Struct("i")
        buf = bytearray(range(5))
        self.assertEqual(f
