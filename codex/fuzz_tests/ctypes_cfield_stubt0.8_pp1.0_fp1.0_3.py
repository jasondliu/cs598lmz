import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_void_p),
                ('z', ctypes.POINTER(S))]

s = S(1)
c = C(2, ctypes.byref(s), ctypes.pointer(s))

c_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(C))

@c_type
def func(c):
    print(c.contents.x, c.contents.y, c.contents.z.contents.x)

func(c)
</code>

