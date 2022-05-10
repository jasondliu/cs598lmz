import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class E(Exception):
    pass

def func_s(s):
    print("called with", s)
    raise E("sorry")

def func_p(p):
    print("called with", p)
    raise E("sorry")

def func_p_s(p, s):
    print("called with", p, s)
    raise E("sorry")

def func_p_p(p1, p2):
    print("called with", p1, p2)
    raise E("sorry")

def func_p_p_p(p1, p2, p3):
    print("called with", p1, p2, p3)
    raise E("sorry")

def func_v(v):
    print("called with", v)
    raise E("sorry")

def func_v_v(v1, v2):
    print("called with", v1, v2)
    raise E("sorry")

def func_v_v_v
