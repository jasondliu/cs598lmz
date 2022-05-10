import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

def callback(x):
    print x

C.callback = ctypes.CFUNCTYPE(None, ctypes.CField)(callback)

C.callback(5)
</code>

