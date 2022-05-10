import ctypes
# Test ctypes.CField for inspecting and accessing ctypes objects.

import _ctypes_test

libc = ctypes.CDLL(ctypes.util.find_library("c"))
class S(ctypes.Structure):
    _fields_ = [("two", ctypes.c_int * 2),
                ("sixteen", ctypes.c_int * 16)]

s = S()
# ... (fill list with numbers 1..32)
for i in range(len(s.sixteen)):
    s.sixteen[i] = i + 1
s.two[1] = 42

for field in s._fields_:
    print(repr(field))

    # implementation detail: for non-pointer ctypes, getattr(s, name) returns
    # a ctypes object that is used to retrieve the value from the raw memory
    # block.
    #
    # In the following he have to fiddle a bit with the C type information.
    cfield = ctypes.CField(field, ctypes.c_int)
    ctype = cfield.type
    assert ctype.
