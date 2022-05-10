import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

print(C.a)
print(C.b)
print(D.a)
print(D.b)
print(D.c)

class E(D):
    _fields_ = [("d", ctypes.c_int)]

print(E.a)
print(E.b)
print(E.c)
print(E.d)

class F(E):
    _fields_ = [("e", ctypes.c_int)]

print(F.a)
print(F.b)
print(F.c)
print(F.d)
print(F.e)

class G(F):
    _fields_ = [("f", ctypes.c_int)]

print(G.a)
print(G.b)
print(G
