import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long

p = S.x
p.__set__(S,  1)
assert p.__get__(S) == 1

p.__delete__(S)

class C(object):
    x = ctypes.c_long()

c = C()
assert c.x == 0

c.x = 1
assert c.x == 1

del c.x
assert c.x == 0

try:
    c.x.contents = 1
except AttributeError:
    pass
else:
    raise AssertionError

# Test for SF bug #922177
ctypes.c_wchar_p.__name__
ctypes.c_wchar_p.__repr__()

# Test support for read-only ctypes.c_char_Array instances

ctypes.c_char_Array_3.from_address(ctypes.addressof(ctypes.c_char(0))).readonly = True
ctypes.c_char_Array_3.from_address(ctypes.add
