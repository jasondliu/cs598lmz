import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long
    y = ctypes.c_long

class c(ctypes.Structure):
    field1 = ctypes.c_int
    field2 = ctypes.c_int

# ctypes.string_at()
ctypes.string_at(0)
ctypes.string_at(0, 0)
ctypes.string_at(0, -1)

ctypes.string_at(ctypes.c_int(), 0)
ctypes.string_at(ctypes.c_int(), -1)

ctypes.string_at(S(), 0)
ctypes.string_at(S(), -1)

# ctypes.wstring_at()
ctypes.wstring_at(0)
ctypes.wstring_at(0, 0)
ctypes.wstring_at(0, -1)

ctypes.wstring_at(ctypes.c_int(), 0)
ctypes.wstring_at(ctypes.c_int(), -1)

ctypes.string_at(S(), 0
