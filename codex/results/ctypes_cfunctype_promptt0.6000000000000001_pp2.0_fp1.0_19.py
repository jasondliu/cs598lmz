import ctypes
# Test ctypes.CFUNCTYPE.
def cb(x, y):
    print(x, y)

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

CB_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(A))
cb_func = CB_FUNC(cb)
cb_func(1, A(2, 3))

class B(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', A)]

CB_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(B))
cb_func = CB_FUNC(cb)
cb_func(1, B(2, A(3, 4)))
