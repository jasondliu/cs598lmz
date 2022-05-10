import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    sys.stdout.write('Hello world!')
    return 1

res = fun()
