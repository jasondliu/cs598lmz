import _struct
# Test _struct.Struct with format strings longer than 128 characters
try:
    _struct.Struct('c'*129)
except ValueError as e:
    pass
else:
    raise Exception('expected ValueError')

# Test _struct.Struct with an empty format string, and when given no format
# string.
try:
    _struct.Struct('')
except ValueError as e:
    pass
else:
    raise Exception('expected ValueError')

s = _struct.Struct()
try:
    s.pack()
except struct.error as e:
    pass
else:
    raise Exception('expected struct.error')


from io import BytesIO
from struct import error, pack
from unittest import TestCase


class StructTest(TestCase):

    def test_pad_string(self):
        s = _struct.Struct('x12s')
        self.assertEqual(s.size, 12)
        self.assertEqual(s.pack('foo'), b'\x00'*12)
        self.assertEqual(s.pack(b'bar'), b'\x
