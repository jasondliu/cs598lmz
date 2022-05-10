import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   return 42

FUNTYPE._argtypes_ = (ctypes.py_object,)

a = fun()
</code>

