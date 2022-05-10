import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(S):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CSimpleType = ctypes.c_int

import inspect
print inspect.isclass(ctypes.CField)
print inspect.isclass(ctypes.CSimpleType)


# class A(ctypes.Structure):
#     _fields_ = [('y', ctypes.c_int)]
#
#
# # ctypes.Structure._fields_.copy()
# # ctypes.Structure.__dict__.dup()
# B = type(A)
#
# b = B(y=1)
# print b.y
#
# c = B()
# print c
#
# c.y = 1
#
# print c.y
#
#
#
#
#
#
# a = A()
# a.y = 1
#
# print a.y
#
