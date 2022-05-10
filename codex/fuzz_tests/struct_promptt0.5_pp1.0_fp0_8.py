import _struct
# Test _struct.Struct.format_size
for fmt in ["b", "h", "i", "l", "q", "B", "H", "I", "L", "Q"]:
    for endian in ["@", "=", "<", ">", "!", "|"]:
        s = _struct.Struct(endian + fmt)
        eq(s.size, s.format_size(endian + fmt))
        eq(s.size, s.format_size(fmt))
        eq(s.size, s.format_size(endian))
        raises(TypeError, s.format_size, endian + fmt + "x")
        raises(TypeError, s.format_size, "x" + endian + fmt)
        raises(TypeError, s.format_size, "x" + fmt)
        raises(TypeError, s.format_size, "")
        raises(TypeError, s.format_size, "x")

# Test _struct.Struct.__new__
s = _struct.Struct("b")
eq(s.format, "b")
eq
