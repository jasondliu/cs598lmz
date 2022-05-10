import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 100
print(fun())
# funs = (FUNTYPE * 5)()
# funs[0] = fun
# print(funs[0]())
