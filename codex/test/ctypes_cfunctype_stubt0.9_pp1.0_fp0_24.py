import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.py_object)]

a = A()
