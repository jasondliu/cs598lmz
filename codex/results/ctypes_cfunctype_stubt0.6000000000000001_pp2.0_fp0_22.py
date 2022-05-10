import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
fun()

# from ctypes import *
# import ctypes
# class A(ctypes.Structure):
#     _fields_ = [("a", ctypes.c_int),
#                 ("b", ctypes.c_int)]
#
# class B(ctypes.Structure):
#     _fields_ = [("b", ctypes.c_int),
#                 ("a", ctypes.c_int)]
# a = A()
# a.a = 2
# a.b = 3
# print(a.a, a.b)
#
# b = B()
# b.a = 2
# b.b = 3
# print(b.a, b.b)
#
# b = ctypes.cast(a, B)
# print(b.a, b.b)
