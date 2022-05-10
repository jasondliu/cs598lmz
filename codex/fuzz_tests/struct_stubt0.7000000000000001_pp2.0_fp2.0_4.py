from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'L'
s.size = 4

import unittest

class Test_struct(unittest.TestCase):
    def test_pack(self):
        data = s.pack(1)
        self.assertEqual(data, b'\x00\x00\x00\x01')

    def test_pack_into(self):
        buff = bytearray(4)
        s.pack_into(buff, 0, 1)
        self.assertEqual(buff, b'\x00\x00\x00\x01')

    def test_unpack(self):
        self.assertEqual(s.unpack(b'\x00\x00\x00\x01'), (1,))

    def test_unpack_from(self):
        self.assertEqual(s.unpack_from(b'\x00\x00\x00\x01', 0), (1,))

if __name__ == '__main__':
    unittest.main()
