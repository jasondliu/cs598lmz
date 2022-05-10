import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int)
    ]

x = X()
x.a = 1
x.b = 2
x.c = 3

print(x.a)
print(x.b)
print(x.c)

try:
    x.d = 4
except AttributeError:
    print("AttributeError")

try:
    x.a = "hello"
except TypeError:
    print("TypeError")

try:
    x.a = None
except TypeError:
    print("TypeError")

try:
    x.a = 1.2
except TypeError:
    print("TypeError")

try:
    x.a = 1 + 2j
except TypeError:
    print("TypeError")

try:
    x.a = 1 + 2j
except TypeError:
    print("TypeError
