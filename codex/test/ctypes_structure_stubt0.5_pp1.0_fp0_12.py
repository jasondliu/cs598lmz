import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class L(ctypes.Structure):
    x = ctypes.c_long

class P(ctypes.Structure):
    _fields_ = [("s", S), ("l", L)]

class Q(ctypes.Structure):
    _fields_ = [("l", L), ("s", S)]

class R(ctypes.Structure):
    _fields_ = [("s", S), ("l", L), ("s2", S)]

class T(ctypes.Structure):
    _fields_ = [("s", S), ("l", L), ("s2", S), ("l2", L)]

class U(ctypes.Structure):
    _fields_ = [("s", S), ("l", L), ("s2", S), ("l2", L), ("s3", S)]

class V(ctypes.Structure):
    _fields_ = [("s", S), ("l", L), ("s2", S), ("l2", L), ("s3", S), ("l3", L)]
