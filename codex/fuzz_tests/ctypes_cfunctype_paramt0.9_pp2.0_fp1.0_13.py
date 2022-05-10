import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def wrapper(f):
    @wraps(f)
    def wrapped(*args):
        return ctypes.c_double(f(*args))
    return wrapped


@ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
def myf(a, b, c, d):
    return 1.0* a + 2.0 * b + 3.0 * c + 4.0 * d
myf = FUNTYPE(myf)
</code>

