import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def f(x, *args):
    return np.sum((x-args)**2)

f_ = FUNTYPE(f)

def f_c(x, args):
    return f_(x, *args)

def f_c_with_args(x):
    return f_c(x, np.ones(2))

def f_c_with_args2(x):
    return f_c(x, np.ones(2)*2)

def g(x):
    return np.sum(x**2)

def g_c(x):
    return g(x)

def g_c_with_args(x):
    return g_c(x)

def g_c_with_args2(x):
    return g_c(x)

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("f_c_with_args(np.ones(2))",
