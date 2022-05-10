import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3)
fun()

# without ctypes
def fun():
    return (1,2,3)
fun()
