import ctypes
# Test ctypes.CFUNCTYPE()
def callback(x):
    print("callback:", x)
ptr = ctypes.CFUNCTYPE(None, ctypes.c_int)(callback)
ptr(5)

# Test ctypes.POINTER(ctypes.CFUNCTYPE())
class C(ctypes.Structure):
    _fields_ = [("callback", ctypes.POINTER(ctypes.CFUNCTYPE(None, ctypes.c_int)))]
c = C()
c.callback = ctypes.pointer(ctypes.CFUNCTYPE(None, ctypes.c_int)(callback))
c.callback.contents(10)

# Test ctypes.Structure with ctypes.CFUNCTYPE()
class D(ctypes.Structure):
    _fields_ = [("callback", ctypes.CFUNCTYPE(None, ctypes.c_int))]
d = D()
d.callback = ctypes.CFUNCTYPE(None, ctypes.c_int)(callback)
d.callback(2)

# Test ctypes.
