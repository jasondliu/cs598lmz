import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double),
                           ctypes.c_int, ctypes.c_int)

def run(func, x0, niter, args=()):
    x0 = np.asarray(x0)
    n = len(x0)

    cfunc = FUNTYPE(func)
    cfunc.restype = ctypes.c_double
    cfunc.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int,
                      ctypes.c_int]

    x = np.zeros((niter+1,n))
    f = np.zeros(niter+1)

    x[0] = x0
    f[0] = cfunc(x0.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), n, 0)

    for k in range(niter):
        x[k+1] = x[k]
        f[k+1] = cfunc(x[k+1].
