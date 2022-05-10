import _struct
# Test _struct.Struct with an unpack_from() method.


class UnpackFromTest(unittest.TestCase):

    def test_packed_size(self):
        self.assertEqual(_struct.Struct('h').size, 2)
        self.assertEqual(_struct.Struct('hHi').size, 6)
        self.assertEqual(_struct.Struct('hHi12s').size, 20)
        self.assertEqual(_struct.Struct('hHi12s3x').size, 23)
        self.assertEqual(_struct.Struct('hHi12s3x9s').size, 32)
        self.assertEqual(_struct.Struct('128s').size, 128)
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('l').size, _struct.calcsize('l'))

    def pack_into(self, format, args, buffer, offset=0):
        _struct.Struct(format).pack_into(buffer, offset, *args)

    def test_pack_into(self):
       
