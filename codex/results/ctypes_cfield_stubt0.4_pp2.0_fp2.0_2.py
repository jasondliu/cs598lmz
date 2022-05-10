import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class D(C):
    _fields_ = [('x', ctypes.c_int),
                ('z', ctypes.c_int)]

s = S()
print(s.x)
s.x = 42
print(s.x)

try:
    s.x = "abc"
except TypeError:
    print("TypeError")

try:
    s.x = 1.0
except TypeError:
    print("TypeError")

try:
    s.x = 1.0 + 2.0j
except TypeError:
    print("TypeError")

try:
    s.x = None
except TypeError:
    print("TypeError")

try:
    s.x = []
except TypeError:
    print("TypeError")

try:
    s.x = {}
except TypeError:
    print("TypeError")

try:
    s.x = ()
except TypeError:
