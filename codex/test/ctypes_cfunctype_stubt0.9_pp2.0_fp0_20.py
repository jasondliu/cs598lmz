import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return int(123) # doesn't get converted to long anymore in 3.0
fun()
