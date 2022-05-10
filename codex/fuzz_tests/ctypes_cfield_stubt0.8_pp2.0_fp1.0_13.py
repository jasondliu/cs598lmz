import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@dont_look_inside
def malloc(T):
    ctypes.pythonapi.PyMem_Malloc.restype = ctypes.POINTER(T)
    ctypes.pythonapi.PyMem_Malloc.argtypes = [ctypes.c_size_t]
    return ctypes.pythonapi.PyMem_Malloc(ctypes.sizeof(T))

@dont_look_inside
def free(p):
    ctypes.pythonapi.PyMem_Free(p)

@dont_look_inside
def cast(obj, T):
    p = malloc(T)
    p.contents = obj
    return p

@dont_look_inside
def ptradd(p, T, i):
    return ctypes.cast(ctypes.addressof(p.contents) + i*ctypes.sizeof(T),
                       ctypes.POINTER(T))

@dont_look_inside
def ptroffset(p, T, i):
    return ctypes.pointer(p.contents)
