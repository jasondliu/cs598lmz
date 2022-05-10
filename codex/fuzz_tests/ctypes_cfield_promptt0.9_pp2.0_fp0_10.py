import ctypes
# Test ctypes.CField instance.
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
class XX(X):
    _fields_ = [('b', ctypes.c_double)]

x = X()
x.a = 42
print(x.a, x.b) # ERROR: no b attribute

xx = XX()
xx.a = 87
print(xx.a, xx.b) # ERROR: no b attribute

try:
    _ctypes_test.get_b(x)
except AttributeError:
    print("No get_b method on x")

try:
    _ctypes_test.get_b(xx)
except:
   import sys
   print("get_b(xx)", sys.exc_info()[1])
