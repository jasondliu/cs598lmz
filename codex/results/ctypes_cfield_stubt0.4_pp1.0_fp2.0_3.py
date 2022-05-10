import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

class F(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int), ('z', ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [('y', ctypes.CField), ('z', ctypes.c_int)]

print(D.y)
print(E.y)
print(F.y)
print(G.y)

print(D.y.offset)
print(E.y.offset)
print(F.y.offset)
print(G.y.offset)

print(D.y.size)
print(E.y.size)
print(F.y.size)
print(G.y.size)
