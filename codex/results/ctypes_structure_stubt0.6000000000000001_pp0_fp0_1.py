import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
S._fields_ = [('x', ctypes.c_int)]

def f(s):
    s.x = 3

def f2(s):
    s.x = 3

def f3(s):
    s.x = ctypes.c_int(3)

def f4(s):
    s.x = ctypes.c_int(3)

def f5(s):
    s.x = 3

def f6(s):
    s.x = 3

def f7(s):
    s.x = 3

def f8(s):
    s.x = 3

def f9(s):
    s.x = 3

def f10(s):
    s.x = 3

def f11(s):
    s.x = 3

def f12(s):
    s.x = 3

def f13(s):
    s.x = 3

def f14(s):
    s.x = 3

def f15(s
