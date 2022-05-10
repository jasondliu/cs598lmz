import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = fun

    class C(object):
        def __call__(self):
            return x
    return C()
res = fun()()
