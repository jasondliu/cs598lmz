import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2)

class MyClass(ctypes.Structure):
    _fields_ = [('fun', FUNTYPE)]
