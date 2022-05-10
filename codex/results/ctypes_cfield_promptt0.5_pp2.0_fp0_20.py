import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.CField * 2)]

print(X.a)
print(X.b)

print(Y.a)
print(Y.b)

print(Z.a)
print(Z.b)

x = X("a", "b")
print(x.a, x.b)

y = Y("a", ("b", "c"))
print(y.a, y.b)

z = Z("a", ("b", "c"))
print(z.a, z.b)

try:
    y = Y("a", ("b", "c",
