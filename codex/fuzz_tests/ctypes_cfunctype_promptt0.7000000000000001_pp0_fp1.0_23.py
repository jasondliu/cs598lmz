import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

################################################################

# Return a pointer to a 32-bit integer in memory
lib.ptr_to_int.restype = POINTER(c_int)

for i in range(5):
    p = lib.ptr_to_int()
    assert p.contents.value == i
    assert p[0] == i
    assert p[0] == c_int.from_address(addressof(p.contents)).value
    assert p[0] == cast(p, POINTER(c_int))[0]

# Return a pointer to a 32-bit float in memory
lib.ptr_to_float.restype = POINTER(c_float)

for i in range(5):
    p = lib.ptr_to_float()
    assert p.contents.value == i * 0.25
    assert p[0] == i * 0.25
    assert p[0] == c_float.from_address(addressof(p.cont
