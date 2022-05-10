import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 1

x = X()
print x.a
x.a = 2
print x.a

class Y(X):
    _fields_ = [("b", ctypes.c_int)]
    def __init__(self):
        X.__init__(self)
        self.b = 3

y = Y()
print y.a
y.a = 4
print y.a
print y.b
y.b = 5
print y.b

class Z(Y):
    _fields_ = [("c", ctypes.c_int)]
    def __init__(self):
        Y.__init__(self)
        self.c = 6

z = Z()
print z.a
z.a = 7
print z.a
print z.b
z.b = 8
print z.b
print z.c
z.c = 9
print z.
