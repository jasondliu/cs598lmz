import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("bla")
    return 0
@FUNTYPE
def bla(*args):
    print(args)
    return args

bla(0, **dict(a=1, b=2))
