import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return {'a': [1, 2, 3]}

fun()

# CHECK: {'a': [1, 2, 3]}
