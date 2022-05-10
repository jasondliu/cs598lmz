import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double))

def c_func_factory(func):
    def c_func(coords, out):
        out[0] = func(*coords)
        return 0
    c_func = FUNTYPE(c_func)
    return c_func


def c_func_map(c_func, coords):
    out = ctypes.c_double()
    c_func(coords, ctypes.byref(out))
    return out.value


def _check_tol(a, b, tol, msg):
    assert abs(a - b) < tol, msg + ' (%.2e < %.2e)' % (abs(a - b), tol)


def test_ndmin_1d():
    f = c_func_factory(lambda x: x)

    xs = np.arange(10).astype(dtype=np.float64)
   
