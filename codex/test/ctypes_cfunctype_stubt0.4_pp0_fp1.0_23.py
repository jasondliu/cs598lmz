import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

class C:
    pass

def callback(arg):
    return arg

C.method = FUNTYPE(callback)

obj = C()
