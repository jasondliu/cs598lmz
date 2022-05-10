import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

my_callback = FUNTYPE(my_callback)

lib.register_callback(my_callback)
print lib.call_callback()

# This is how you would do it with ctypes.pythonapi:
# def my_callback(a, b):
#     print "my_callback was called with %d and %d" % (a, b)
#     return a + b
# 
# my_callback = ctypes.pythonapi.PyCFunction_NewEx(my_callback, None, None)
# lib.register_callback(my_callback)
# print lib.call_callback()
