import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__bases__)

try:
    C.x = 1
except TypeError:
    print("TypeError")

try:
    C.x.__doc__ = "hello"
except AttributeError:
    print("AttributeError")

try:
    C.x.__name__ = "hello"
except AttributeError:
    print("AttributeError")

try:
    C.x.__module__ = "hello"
except AttributeError:
    print("AttributeError")

try:
    C.x.__dict__ = {}
except AttributeError:
    print("AttributeError")

try:
    C.x.__slots__ = ()
except AttributeError:
    print("AttributeError")

try:
    C.x.__weakref__ = None
except AttributeError:

