import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise Exception('abc')
try:
    fun()
except Exception as exc:
    print(exc)
