import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', S)]

print C.x
print C.x.x
print type(C.x.x)
print isinstance(C.x.x, type)
print isinstance(C.x.x, ctypes.CField)
print ctypes.CField(ctypes.c_int(), 0)
print ctypes.CField(ctypes.c_int(), 0).__ctypes_from_outparam__()
