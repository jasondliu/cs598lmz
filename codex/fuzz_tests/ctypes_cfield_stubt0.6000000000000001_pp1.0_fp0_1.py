import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
#ctypes.CField(S, 'x', ctypes.c_int)

class S2(ctypes.Structure):
    _fields_ = [('y', ctypes.POINTER(S))]

print(S2.y.from_param)

#ctypes.CField(S2, 'y', ctypes.POINTER(S))
#ctypes.CField(S2, 'y', ctypes.POINTER(S), ctypes.c_void_p)

#ctypes.CField = type(S2.y)
#ctypes.CField(S2, 'y', ctypes.POINTER(S))

#ctypes.CField = type(S.x)
#ctypes.CField(S, 'x', ctypes.c_int)

#ctypes.CField = type(S2.y)
#ctypes.CField(S2, 'y', ctypes.POINTER(S))

#ctypes.CField = type(S2.y)
#ctypes.CField(S2
