import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
s = fun
s()

s = ctypes.pythonapi.PyObject_Str
s.restype = ctypes.py_object

s(fun)
</code>

