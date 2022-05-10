import _struct
# Test _struct.Struct type
# test classes currently derive from object to allow test output to be printed
class StructTest(object):
    def __init__(self, format_char, format, size, alignment, format_args, values, to_str=str):
        self.format_char = format_char
        self.format = format
        self.size = size
        self.alignment = alignment
        self.format_args = format_args
        self.values = values
        self.to_str = to_str

    def pack_test(self):
        s = _struct.Struct(self.format)
        packed = s.pack(*self.values)
        expected = struct.pack(self.format, *self.values)
        self.assertEqual(packed, expected)
        self.assertEqual(s.size, self.size)
        self.assertEqual(s.pack_into(bytearray(), 0, *self.values), None)

    def unpack_test(self):
        s = _struct.Struct(self.format)
        packed = struct.pack(self.
