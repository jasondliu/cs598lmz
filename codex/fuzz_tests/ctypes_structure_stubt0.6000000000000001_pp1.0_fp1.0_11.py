import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p

class S2(ctypes.Structure):
    x = ctypes.c_char_p

class X(ctypes.Structure):
    _fields_ = [('s', S)]

class X2(ctypes.Structure):
    _fields_ = [('s', S2)]

class Y(ctypes.Structure):
    _fields_ = [('s', S)]
    _pack_ = 1

class Y2(ctypes.Structure):
    _fields_ = [('s', S2)]
    _pack_ = 1

class Z(ctypes.Structure):
    _fields_ = [('s', S)]
    _pack_ = 2

class Z2(ctypes.Structure):
    _fields_ = [('s', S2)]
    _pack_ = 2

class W(ctypes.Structure):
    _fields_ = [('s', S)]
    _pack_ = 4

class W2(ctypes.Structure):
    _fields_ = [('s
