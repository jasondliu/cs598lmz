import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 1
def fun4(x):
    return x
fun5 = FUNTYPE(fun4)
assert fun5(5) == 5
