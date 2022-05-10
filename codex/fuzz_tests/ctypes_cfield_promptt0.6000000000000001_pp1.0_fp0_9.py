import ctypes
# Test ctypes.CField
import ctypes
class foo(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class bar(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.CField)]

f = foo()
b = bar()
f.a = 1
f.b = 2
b.a = 1
b.b = f
print b.b.b
# Test ctypes.CField
import ctypes

class foo(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class bar(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.CField)]

f = foo()
b = bar()
f.a = 1
f.b = 2
b.a = 1
b.b = f
print b.b.
