import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return Py_RETURN_TRUE

@FUNTYPE
def fun2():
    return Py_None

class A:
    def __call__(self):
        return None
    def __len__(self):
        return 2

a = A()
