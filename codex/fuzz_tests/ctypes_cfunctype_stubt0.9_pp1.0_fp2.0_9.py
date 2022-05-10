import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    import warnings
    warnings.warn("i was not expecting to live")
import gc
class X(object):
    def __del__(self):
        fun()
x = X()
del x
gc.collect()
