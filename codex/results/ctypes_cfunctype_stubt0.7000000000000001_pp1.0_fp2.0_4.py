import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 1

def f():
  assert ctypes.cast(fun, ctypes.c_void_p).value == ctypes.addressof(fun)
  return fun()

f()
