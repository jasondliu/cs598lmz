import _struct
# Test _struct.Struct
pa = _struct.Struct("hHiIlLfd")
o = pa.pack(1, 2, 3, 4, 5, 6, 7.125, 8.25)
