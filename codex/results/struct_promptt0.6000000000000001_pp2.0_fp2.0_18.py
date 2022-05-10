import _struct
# Test _struct.Struct
s = _struct.Struct("b")
s.format
s.size
s.align
s = _struct.Struct("=b")
s.format
s.size
s.align
s = _struct.Struct("<b")
s.format
s.size
s.align
s = _struct.Struct("@b")
s.format
s.size
s.align
s = _struct.Struct("b", _struct.LITTLE_ENDIAN)
s.format
s.size
s.align
s = _struct.Struct("b", _struct.BIG_ENDIAN)
s.format
s.size
s.align
# Test _struct.pack
s = _struct.Struct("b")
s.pack(1)
s.pack(-1)
s = _struct.Struct("<b")
s.pack(1)
s.pack(-1)
s = _struct.Struct(">b")
s.pack(1)
s.pack(-1)
s = _struct.Struct("@b")
s.pack(1)
s.
