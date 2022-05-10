import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))

@FUNTYPE
def f(n, m, x, p):
    p[0] = 1.0
    p[1] = 2.0
    return np.linalg.norm(x)

@FUNTYPE
def fp(n, m, x, p):
    return np.linalg.norm(x)

@FUNTYPE
def g(n, m, x, p):
    p[0] = 1.0
    p[1] = 2.0
    return np.linalg.norm(x)

@FUNTYPE
def gp(n, m, x, p):
    return np.linalg.norm(x)

@FUNTYPE
def h(n, m, x, p):
    p[0] = 1.0
    p[1] = 2.0
    return np.linalg.norm
