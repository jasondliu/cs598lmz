import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    def __init__(self):
        self.c = ctypes.c_int(1)

x = X()
print x.c
print x._fields_
print x._b_needsfree_

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int), ("c", ctypes.c_int)]

y = Y()
print y.c
print y._fields_
print y._b_needsfree_

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

z = Z()
print z.b
print z._fields_
print z._b_needsfree_

class A(ctypes.Structure):
    _fields_ = [("a",
