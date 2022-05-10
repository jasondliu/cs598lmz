import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class S2(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(s):
    s.x = 1
    s.y = 2
    s.z = 3

def g(s):
    s.x = 1
    s.y = 2
    s.z = 3

def h(s):
    s.x = 1
    s.y = 2
    s.z = 3

def i(s):
    s.x = 1
    s.y = 2
    s.z = 3

def j(s):
    s.x = 1
    s.y = 2
    s.z = 3

def k(s):
    s.x = 1
    s.y = 2
    s.z = 3

def l(s):
    s.x = 1
    s.y
