import ctypes
# Test ctypes.CField!
# (first, remove what was installed here before)
try:
    del ctypes.CField
except AttributeError: pass
try:
    del ctypes._CField
except AttributeError: pass
# then, get the _CField class (without asking ctypes for it)
cf = ctypes._CField
# then,let's define a CField!

class CField(cf):
    _pack_ = 1
    _type_ = "L"
    _length_ = 4
    _is_packed_ = True

# Let's try some basic operations

CF = CField.from_param(0x01020304)

# CField(0x01020304) == CField(0x01020304)
assert CF == ctypes._CField(0x01020304)
# CField(0x01020304) == 0x01020304
assert CF == 0x01020304
# 0x01020304 == CField(0x01020304)
assert 0x01020304 == CF
# CField(0x01020304) != CField
