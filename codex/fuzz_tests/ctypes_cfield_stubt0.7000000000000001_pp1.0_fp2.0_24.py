import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

ctypes.CUnion = type(C)

class D(ctypes.CField):
    pass

try:
    3 * C.x
except TypeError, details:
    print details

try:
    C.x ** 2
except TypeError, details:
    print details

try:
    C.x.real
except AttributeError, details:
    print details

try:
    C.x.imag
except AttributeError, details:
    print details

try:
    C.x.conjugate()
except AttributeError, details:
    print details

try:
    ctypes.c_int.__new__(D)
except TypeError, details:
    print details

try:
    ctypes.c_int.__new__(D, 42)
except TypeError, details:
    print details

try:
    ctypes.c_int
