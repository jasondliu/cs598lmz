import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes, 'x')
    y = ctypes.c_int.in_dll(ctypes, 'y')
    #x = ctypes.c_int.in_dll(ctypes, 'x')

print S.x, S.y
