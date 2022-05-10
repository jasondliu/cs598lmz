import _struct
# Test _struct.Struct with format string and optional endianness
# argument.

def test_struct_with_endianness(fmt, expected):
    for endianness in ('@', '=', '<', '>', '!'):
        s = _struct.Struct(endianness + fmt)
        eq(s.size, expected[0])
        eq(s.format, expected[1])

def test_struct_with_format(fmt, expected):
    s = _struct.Struct(fmt)
    eq(s.size, expected[0])
    eq(s.format, expected[1])

def test_struct_with_format_and_endianness(fmt, expected):
    s = _struct.Struct(fmt, '@')
    eq(s.size, expected[0])
    eq(s.format, expected[1])

def test_struct_with_endianness_and_format(fmt, expected):
    s = _struct.Struct('@' + fmt)
    eq(s.size, expected[0])
    eq(
