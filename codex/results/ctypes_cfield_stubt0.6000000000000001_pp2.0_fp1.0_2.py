import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(object):
    def __init__(self):
        self.x = ctypes.c_int(1)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.PyCSimpleType = type(ctypes.c_int)

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class H(ctypes.Structure):
    pass

class I(object):
    def __init__(self):
        self.x = 1

class J(ctypes.Structure):
    pass

class K(object):
    def __init__(self):
        self.x = ctypes.c_int(1)

class L(ctypes.Structure):
    pass

