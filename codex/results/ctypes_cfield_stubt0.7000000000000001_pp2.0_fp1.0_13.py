import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(S):
    _fields_ = [('y', ctypes.c_int)]

# this works
#D.y.offset

# this works
#D.y.size

# this fails
D.y.offset + D.y.size # TypeError: unsupported operand type(s) for +: 'int' and 'int'
</code>
Python 3.8.0

