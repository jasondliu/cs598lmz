import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hi"

dll = ctypes.CDLL("./dll.dll")
dll.fun.restype = ctypes.py_object
dll.fun.argtypes = [ctypes.py_object]
dll.fun(fun)
</code>

