import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.Structure._fields_
ctypes.Structure._fields_[:]

t1 = ctypes.c_int * 3
type(t1)
ctypes.Array = type(t1)
type(t1), type(t1())

ctypes.POINTER = ctypes.c_int * 3
ctypes.POINTER = type(ctypes.pointer(ctypes.c_int()))

ctypes.c_int(1).value == ctypes.c_int(1)

#ctypes.c_int()
ctypes.c_int(1).value

ctypes.cast(1, ctypes.c_int)

ctypes.c_int(10) + ctypes.c_int(1)
ctypes.c_int(10) - ctypes.c_int(1)
ctypes.c_int(10) * ctypes.c_int(1)
ctypes.c_int(10) / ctypes.c_int(1)
ctypes.c_int(10) % ctypes.c_
