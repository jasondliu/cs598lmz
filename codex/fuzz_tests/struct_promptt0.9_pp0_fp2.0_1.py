import _struct
# Test _struct.Struct
from test import support
Sc = _struct.Struct
# Sc(format) is the same as struct.Struct(format).
with support.check_warnings(('', BytesWarning)):
    with support.captured_stdout() as s:
        s = Sc("!bhi")
    self.assertEqual(s.format, '!bhi')
    self.assertEqual(repr(s), "Struct('!bhi')")
    self.assertEqual(s.__sizeof__(), Sc.__sizeof__())
    # s.size is the size of a single element
    self.assertEqual(s.size, 7)
    # s.unpack(str) is the same as s.unpack_from(str, 0)
    with support.check_warnings(('', BytesWarning)):
        d = s.unpack(b'\xaa\x00\x12\x34\x00\x00\xbb')
    self.assertEqual(d, (0xaa, 0x1234, 0xbb))
   
