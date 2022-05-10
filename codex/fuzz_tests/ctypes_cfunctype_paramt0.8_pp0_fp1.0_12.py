import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
sin_c = FUNTYPE(sin)

x = 0.3

%timeit np.sin(x)
%timeit sin(x)
%timeit sin_c(x)

%timeit np.sin(X)
%timeit sin(X)

%timeit np.sin(X)
%timeit sin(X)
</code>

