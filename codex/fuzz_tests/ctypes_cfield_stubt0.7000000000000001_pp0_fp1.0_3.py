import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', S)]

ctypes.CStruct = type(C)

class C2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class C3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class C4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.Structure._anonymous_ = {"C2": C2, "C3": C3, "C4": C4}

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('C2', C2),
                ('C3', C3),
                ('C4', C4),
                ('y', ctypes.c_int)]

ctypes.Union._anonymous_ = {"C2": C2, "C3": C3, "C4": C4}

