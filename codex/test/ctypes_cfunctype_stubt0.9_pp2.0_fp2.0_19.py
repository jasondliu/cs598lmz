import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def fn():
    return 1

x = fun
x()
# array(42, dtype=object)

