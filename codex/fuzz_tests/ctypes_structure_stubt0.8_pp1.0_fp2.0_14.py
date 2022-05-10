import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(DLL, "x")

S()
S().x
S().x = 4
S().x

val = ctypes.c_int.in_dll(DLL, "x")
val.value
val.value = 4
val.value

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    x = ctypes.c_int.in_dll(DLL, "x")

S()
S().x
S().x = 4
S().x

# ===========
