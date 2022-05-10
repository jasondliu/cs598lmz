import ctypes
# Test ctypes.CField is automatically generated.

import _ctypes_test

get_cfield = _ctypes_test.lib.get_cfield
get_cfield.argtypes = ctypes.c_void_p, ctypes.c_void_p
get_cfield.restype = ctypes.c_void_p

class CField1(ctypes.CField): pass
class CField2(_ctypes_test.Structure): pass
class CField3(_ctypes_test.MyUnion): pass
class CField4(ctypes.Union): pass

try:
    union_cfield = get_cfield(_ctypes_test.Structure, '$union_cfield')
except ValueError:
    raise ValueError(
        "TestDict.get(key) -> value. the key '$union_cfield' should not be there")

try:
    union_cfield1 = get_cfield(CField1, '$union_cfield')
except ValueError:
    raise ValueError(
        "TestDict.get(key) -> value. the key '
