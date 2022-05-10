import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]

class C(ctypes.Structure):
    S_inst = S()
    _fields_ = [('S_inst', S)]

c = C()
c.S_inst.x = 1
