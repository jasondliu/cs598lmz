import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)
def my_func(x):
    return int(x)

cfunc = FUNTYPE(my_func)

print cfunc(1.2)

# class MyClass(object):
#     def __init__(self, x):
#         self.x = x
#
#     def my_func(self, x):
#         return int(x)
#
# cfunc = FUNTYPE(MyClass(1).my_func)
#
# print cfunc(1.2)
