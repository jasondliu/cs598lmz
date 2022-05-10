import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))


def function(x):
    return  np.sum(x**2)


def jacobian(x):
    return  2*x


import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int)


def c_function(x,n,p):
    #print x, n, p
    xs = np.fromiter(x, ctypes.c_double, n*p)
    #print xs, xs.shape, xs.dtype
    res = function(xs)
    return  res


def c_jacobian(x,n,p):
    #print x, n, p
    xs = np.fromiter(x, ctypes.c_double, n*p)
    #print xs, xs.shape, xs.dtype
    res = jacobian
