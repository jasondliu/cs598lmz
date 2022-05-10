import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def cfun(f):
    return FUNTYPE(f)

def cfun_1(f):
    return FUNTYPE(lambda x: f(x))

def cfun_2(f):
    return FUNTYPE(lambda x, y: f(x, y))

def cfun_3(f):
    return FUNTYPE(lambda x, y, z: f(x, y, z))

def cfun_4(f):
    return FUNTYPE(lambda x, y, z, u: f(x, y, z, u))

def cfun_5(f):
    return FUNTYPE(lambda x, y, z, u, v: f(x, y, z, u, v))

def cfun_6(f):
    return FUNTYPE(lambda x, y, z, u, v, w: f(x, y, z, u, v, w))

def cfun_7(f):
    return FUNTYPE(lambda x, y, z, u, v,
