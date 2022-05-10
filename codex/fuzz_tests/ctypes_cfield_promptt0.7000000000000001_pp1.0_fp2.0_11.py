import ctypes
# Test ctypes.CField
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

x = X()

print(dir(x))
print(x.a)
print(X.a)
print(x.a.__class__)
print(X.a.__class__)
print(ctypes.CField.__class__)

print(issubclass(type(x.a), ctypes.CField))
print(issubclass(type(X.a), ctypes.CField))
print(issubclass(ctypes.CField, ctypes.CField))

try:
    x.a = 1
except TypeError:
    print("x.a = 1: TypeError")

try:
    X.a = 1
except TypeError:
    print("X.a = 1: TypeError")

try:
    ctypes.CField = 1
except TypeError:
    print("ctypes.CField = 1: TypeError")

# XXX We need to check that we
