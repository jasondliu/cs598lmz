import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return foo
assert fun() is None
try:
    import _codecs
except ImportError:
    pass
