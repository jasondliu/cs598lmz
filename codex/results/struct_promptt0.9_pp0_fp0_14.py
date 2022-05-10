import _struct
# Test _struct.Struct
ms = _struct.Struct('<8s2s1s280s')
# And test casting from C to Python by calling calcsize.
t = ms.calcsize('<2s1s1s')
assert isinstance(t, int)
