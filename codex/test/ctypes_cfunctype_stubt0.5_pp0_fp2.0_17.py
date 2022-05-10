import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def set_fun_as_attr(obj, name, fun):
    ctypes.pythonapi.PyObject_SetAttrString(ctypes.py_object(obj), name, fun)

class A(object):
    def __init__(self):
        set_fun_as_attr(self, "fun", fun)

a = A()
