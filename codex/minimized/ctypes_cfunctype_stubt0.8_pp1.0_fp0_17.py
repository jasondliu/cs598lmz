import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(s1, s2):
    return s1 + ' ' + s2
fun('spam', 'and eggs')
