import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world"

print(fun())

#import ctypes
#FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
#@FUNTYPE
#def fun(a, b):
#    return a + b
#
#print(fun(1, 2))

#import ctypes
#FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)
#@FUNTYPE
#def fun(a, b, c):
#    return a + b + c
#
#print(fun(1, 2, 3))

#import ctypes
#FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object, ctypes.py_object)
#@FUNTYPE
#def fun(a, b, c, d):
#    return a + b +
