import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong
    z = ctypes.c_longlong

def f(s):
    return (s.x, s.y, s.z)

def access_to_instance_attr():
    s = S(1,2,3)
    return f(s)

