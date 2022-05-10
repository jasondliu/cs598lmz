import _struct
# Test _struct.Struct with a non-native format
import _struct
import sys
try:
    _struct.Struct('I').pack(1)
except _struct.error:
    pass
else:
    raise Exception('_struct.Struct("I").pack(1) must not work on a non-native format')


class StructTest(unittest.TestCase):
    def check_sizeof(self, code, size):
        self.assertEqual(_struct.calcsize(code), size)

    def check_unpack(self, code, data, result):
        # check native order
        s = _struct.Struct(code)
        self.assertEqual(s.unpack(data), result)
        self.assertEqual(s.unpack_from(data, 0), result)
        self.assertEqual(s.unpack_from(bytearray(data), 0), result)
        self.assertEqual(s.unpack_from(memoryview(data), 0), result)
        self.assertEqual(s.unpack_from(array.array('b', data
