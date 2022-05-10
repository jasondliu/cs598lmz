import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'test'
ret=fun()
print(ret)
FUNTYPE = ctypes.CFUNCTYPE(None)
@FUNTYPE
def fun():
   print("HEL")
fun()
