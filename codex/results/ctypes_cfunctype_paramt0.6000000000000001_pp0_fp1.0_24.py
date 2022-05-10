import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_f(f):
    f_c = FUNTYPE(f)
    return f_c

def bisection_method(a, b, f, n, tol):
    fa = f(a)
    fb = f(b)
    assert fa * fb < 0, "f(a) and f(b) have the same sign"
    x = (a + b) / 2
    fx = f(x)
    for i in range(n):
        if fx == 0 or (b - a) / 2 < tol:
            return x
        elif fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
        x = (a + b) / 2
        fx = f(x)
    return x

def falsi_method(a, b, f, n, tol):
    fa = f(a)
    fb = f(b)
    assert fa
