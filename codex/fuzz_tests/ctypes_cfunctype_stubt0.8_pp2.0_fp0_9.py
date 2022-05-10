import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise ValueError("globals()")
try:
    fun()
except ValueError:
    pass
print("OK")
