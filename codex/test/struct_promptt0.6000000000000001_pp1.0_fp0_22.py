import _struct
# Test _struct.Struct.format and _struct.pack_into
class TestStruct(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.Struct('x').format, 'x')
        self.assertEqual(_struct.Struct('xy').format, '2s')
        self.assertEqual(_struct.Struct('xyz').format, '3s')
        self.assertEqual(_struct.Struct('xyzw').format, '4s')
        self.assertEqual(_struct.Struct('xyzwv').format, '5s')
        self.assertEqual(_struct.Struct('xyzwvu').format, '6s')
        self.assertEqual(_struct.Struct('xyzwvut').format, '7s')
        self.assertEqual(_struct.Struct('xyzwvuts').format, '8s')
        self.assertEqual(_struct.Struct('xyzwvutsr').format, '9s')
