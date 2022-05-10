import _struct
# Test _struct.Struct

class TestStruct(unittest.TestCase):
    def helper(self, format, num, args, eargs):
        self.assertEqual(num, _struct.calcsize(format))
        s = _struct.Struct(format)
        self.assertEqual(num, len(s.pack(*args)))
        self.assertEqual(num, len(s.pack_into('\0'*num, 0, *args)))
        self.assertEqual(num, len(s.pack_into(buffer('\0'*num), 0, *args)))
        self.assertEqual(num,
                         len(s.pack_into(array.array('c', '\0'*num), 0, *args)))
        self.assertEqual(eargs, s.unpack(s.pack(*args)))
        self.assertEqual(eargs, s.unpack_from(s.pack(*args), 0))
        self.assertEqual(eargs, s.unpack_from('\0'*num+s.pack(*args), num))


