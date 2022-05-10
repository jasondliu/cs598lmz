from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('3s3sHH')

data = b'\x01\x02\x03abc\x00\x01\x00\x02'
s.unpack(data)

_make_struct = Struct.__new__


def __make_struct(fmt):
    try:
        return struct_cache[fmt]
    except KeyError:
        struct_cache[fmt] = _make_struct(fmt)
        return struct_cache[fmt]


Struct.__new__ = __make_struct


class StructTestCase(unittest.TestCase):
    def test_structobject(self):
        self.assertEqual(struct.pack('hhhh', 1, 2, 3, 4), b'\x01\x00\x02\x00\x03\x00\x04\x00')
        self.assertEqual(struct.unpack('hhhh', b'\x01\x00\x02\x00\x03\x00\x04\x00'), (1, 2, 3,
