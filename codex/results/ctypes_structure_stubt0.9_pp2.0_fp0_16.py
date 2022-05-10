import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()

lib = ctypes.cdll.LoadLibrary('./point_operators.so')
lib.set_y_to_half.argtypes = (ctypes.POINTER(S),)
lib.set_y_to_half.restype = ctypes.POINTER(S)

lib.set_z_to_half.argtypes = (ctypes.POINTER(S),)
lib.set_z_to_half.restype = ctypes.POINTER(S)

s = S()
lib.set_y_to_half(ctypes.byref(s))
lib.set_z_to_half(ctypes.byref(s))
print(s.x, s.y, s.z)
