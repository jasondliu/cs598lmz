import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 1,2,3

class X(object):
    @classmethod
    def method(cls): pass

