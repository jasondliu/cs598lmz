import ctypes
# Test ctypes.CField
assert(ctypes.CField(ctypes.c_int).__getitem__(()) == ctypes.c_int)
assert(ctypes.CField(ctypes.c_int, size=16).__getitem__(()) == ctypes.c_int * 2)
assert(ctypes.CField(ctypes.c_int, size=16).__getitem__((0,)) == ctypes.c_int)
assert(ctypes.CField(ctypes.c_int, size=16).__getitem__((1,)) == ctypes.c_int)
assert(ctypes.CField(ctypes.c_int, size=16).__getitem__((1, 2)) == ctypes.c_int * 3)
assert(ctypes.CField(ctypes.c_int, size=16).__getitem__((1, 2, 3)) == ctypes.c_int * 4)
assert(ctypes.CField(ctypes.c_int, size=16).__getitem__((1, 2, 3, 4)) == ctypes.c
