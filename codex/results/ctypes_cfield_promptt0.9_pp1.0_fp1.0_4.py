import ctypes
# Test ctypes.CField.
# Unfortunately, we cannot test this on the standard structure
# types provided by the platform because their contents are not
# guaranteed to be only those explicitly specified by the standard.

# See Python bug 909338 (fixed)

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ushort)]

f = S._fields_[0]
assert isinstance(f, ctypes.CField)
assert repr(f) == "<CField 'x' of type 'c_ushort' at %#x>" % (id(f),)

# The following selectors are defined:
# name, type, offset, input_converter
for sel in "name", "type", "offset", "input_converter":
    v = getattr(f, sel)
    assert v == "x" or v == ctypes.c_ushort or v == 0 or v is ctypes.c_ushort.from_param
# "restype" seems to be implementation-dependant.

assert f.pack_for_pair(0, 0
