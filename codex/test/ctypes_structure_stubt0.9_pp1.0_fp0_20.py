import ctypes

class S(ctypes.Structure):
    x = 0 # This is not accepted by the compiler.
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Union):
    x = 0 # This is not accepted by the compiler.
    _fields_ = [('x', ctypes.c_int)]

class A(ctypes.Structure):
    x = 0 # This is not accepted by the compiler.
    _fields_ = [('x', ctypes.c_int)]
    _anonymous_ = []

class B(A):
    _anonymous_ = ['foo']

try:
    B()
except:
    pass
# So now we must have a class definition for "B", but with
# _anonymous_ = []
try:
    S()
except:
    pass
D()

# This one segfaults
# S._fields_[0] = ('a', ctypes.c_int)

# This raises an error because we cannot remove anonymous fields:
try:
    del B._anonymous_[:]
except TypeError as details:
    print
