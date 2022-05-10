import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(C):
    _fields_ = [('x', ctypes.c_long)]

class F(C):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_int)]

class G(C):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_int)]
    _anonymous_ = ['x']

class H(C):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_int)]
    _anonymous_ = ['x', 'y']

class I(C):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_int)]
    _anonymous_ = ['x', 'y', 'z']

class J
