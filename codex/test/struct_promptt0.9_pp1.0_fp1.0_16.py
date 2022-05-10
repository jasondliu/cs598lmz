import _struct
# Test _struct.Struct.
s = _struct.Struct("l")
if s.size != _struct.calcsize("l"):
    print("error in _struct.Struct.size")
if repr(s) != "_struct.Struct(l)":
    print("error in _struct.Struct.__repr__")
if s.format != "l":
    print("error in _struct.Struct.format")
if s.pack(1) != b"\1\0\0\0\0\0\0\0":
    print("error in _struct.Struct.pack")
try:
    s.pack(1, 2)
except TypeError:
    pass
else:
    print("error in _struct.Struct.pack")
if s.pack_into(b"\0"*32, 0, 1) != 32 or \
   b"\1\0\0\0\0\0\0\0" != b"\0"*32:
    print("error in _struct.Struct.pack_into")
