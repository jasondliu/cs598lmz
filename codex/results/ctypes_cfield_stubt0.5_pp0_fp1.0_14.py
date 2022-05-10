import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(C):
    _fields_ = C._fields_ + [('y', ctypes.c_int)]

# this works
C._fields_.append(('y', ctypes.c_int))

# this does not
D._fields_.append(('z', ctypes.c_int))
</code>
The error is:
<code>TypeError: _fields_ must be a sequence of (name, C type) pairs
</code>


A:

<code>ctypes.Structure._fields_</code> is a tuple, not a list. You can't use <code>append</code> on a tuple.

