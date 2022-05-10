import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(self, x):
    self.x = x

def g(self, x):
    self.x = x

s = S()
print(ctypes.addressof(s))

try:
    S.f = f
except TypeError as e:
    print(e)

S.f = ctypes.CFUNCTYPE(None, ctypes.POINTER(S), ctypes.c_int)(f)
print(ctypes.addressof(s))

try:
    S.g = g
except TypeError as e:
    print(e)

S.g = ctypes.CFUNCTYPE(None, ctypes.POINTER(S), ctypes.c_int)(g)
print(ctypes.addressof(s))
