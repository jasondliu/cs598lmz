import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double))

def fun(N, a):
    """sum of array"""
    return sum(a[i] for i in range(N))

fun_c = FUNTYPE(fun)

libc = ctypes.CDLL('libc.so.6')
cfun_c = libc.qsort
cfun_c.argtypes = (
    ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, FUNTYPE,
)
cfun_c.restype = None

N = 100000
a = (ctypes.c_double*N)(*range(N)) # need to initialise memory!
cfun_c(a, N, 8, fun_c)
print(a[:10]) # [999.0, 998.0, 997.0, ..., 1.0, 0.0]
</code>
The last coefficient is proportional to the machine word size, in this case 8 bytes
