import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'a'
def call(fun):
    #print(fun(fun))
    return fun(fun)
call(fun)

#print(call(fun))
