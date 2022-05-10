import _struct
# Test _struct.Struct()
s = _struct.Struct("x y z")
packed = s.pack(1, 2, 3.0)
