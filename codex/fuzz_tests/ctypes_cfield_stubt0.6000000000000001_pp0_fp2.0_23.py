import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('y', ctypes.c_float)]

ctypes.CField = type(D.y)

# test if the new type is now working
class E(ctypes.Structure):
    _fields_ = [('a', ctypes.CField),
                ('b', ctypes.CField)]

ctypes.CField = type(E.a)

class F(ctypes.Structure):
    _fields_ = [('c', ctypes.CField),
                ('d', ctypes.CField)]

ctypes.CField = type(F.c)

# this should fail
class G(ctypes.Structure):
    _fields_ = [('e', ctypes.c_char),
                ('f', ctypes.CField)]

# this should fail
class H(ctypes.Structure):
    _fields_ = [('g', ctypes.CField),
                ('h', ctypes.c_char)]

# this should work
class I(ct
