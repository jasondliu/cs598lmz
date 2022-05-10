import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CData = type(S())

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

# Test that ctypes.Structure can be subclassed, and that
# the subclass instances can be created and destroyed.
class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(C):
    _fields_ = [('z', ctypes.c_int),
                ('t', ctypes.c_int)]

class F(E):
    _fields_ = [('u', ctypes.c_int)]

class G(F):
    _fields_ = [('v', ctypes.c_int)]

class H(F):
    _fields_ = [('v', ctypes.c_int)]

for cls in [C, D, E, F, G, H]:
    for i in range(100):
        cls()

# Test that the _fields_ attribute can be
