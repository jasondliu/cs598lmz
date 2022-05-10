import _struct
# Test _struct.Struct
s = _struct.Struct("c1")
a = s.pack("a")
b = s.pack("b")
