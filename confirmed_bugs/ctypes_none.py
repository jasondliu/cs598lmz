import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

while True:
    fun()
