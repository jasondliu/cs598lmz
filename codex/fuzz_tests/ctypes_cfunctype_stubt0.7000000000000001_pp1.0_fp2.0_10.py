import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    try:
        raise NotImplementedError
    except:
        raise

try:
    fun()
except NotImplementedError:
    pass
</code>

