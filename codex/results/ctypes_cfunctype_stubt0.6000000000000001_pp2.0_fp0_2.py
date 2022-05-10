import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello world')
    return None
fun()

print(type(fun))
print(fun.__class__)

from ctypes import pythonapi
print(pythonapi.PyCFunction_New)

# from ctypes import *
#
# class MyCFUnType(CFUNCTYPE):
#     def __init__(self, *args):
#         CFUNCTYPE.__init__(self, *args)
#
#     def __call__(self, *args):
#         print("call", args)
#         return CFUNCTYPE.__call__(self, *args)
#
# fun = MyCFUnType(c_int, c_int)(lambda x, y: x + y)
# print(fun(1, 2))

from ctypes import *

class MyCFUnType(CFUNCTYPE):
    def __init__(self, *args):
        CFUNCTYPE.__init__(self, *args)

    def __call__(self, *args):
        print("call", args
