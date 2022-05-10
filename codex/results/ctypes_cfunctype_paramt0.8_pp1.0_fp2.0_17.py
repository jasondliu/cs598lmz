import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_double,
    ctypes.c_int,
    np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")
)

# Describe the function's argument and return types.
c_function = FUNTYPE(
    ctypes.CDLL("c_function", mode=ctypes.RTLD_GLOBAL).c_function)
c_inplace = FUNTYPE(
    ctypes.CDLL("c_function", mode=ctypes.RTLD_GLOBAL).c_inplace
)

# Call the function.
a = np.random.rand(5)
c_function(2, a)
c_inplace(2, a)
</code>
c_function.pyx
<code>def c_function(x, y):
    cdef int xc = x
    cdef int i
    if xc &lt; 1:
        return -1.0

    cdef double[:] yc = y
    cdef double retval = 0.0
    for i in
