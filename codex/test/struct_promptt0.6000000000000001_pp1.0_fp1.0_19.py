import _struct
# Test _struct.Struct()
s = _struct.Struct("x")
try:
    s.pack(1, 2)
except TypeError:
    pass
else:
    print("_struct.Struct().pack() did not raise TypeError")

try:
    s.unpack("x")
except TypeError:
    pass
else:
    print("_struct.Struct().unpack() did not raise TypeError")

try:
    s.iter_unpack("xxxx")
except TypeError:
    pass
else:
    print("_struct.Struct().iter_unpack() did not raise TypeError")
