import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_int)

def sample(n):
    C = np.array([np.random.choice(np.arange(n)) for _ in range(n)])
    return (C,1/n * np.dot(C,C))

def wrapper(f):
    f = FUNTYPE(f)
    def wrapped(n):
        return f(n)
    return wrapped

@wrapper
def sample_c(n):
    C = np.random.choice(n,n)
    for i in range(1,n):
        C[i] += C[i-1]
    return (C[-1] + 0.0)/n

@jit("f8(i4)")
def sample_numba(n):
    C = np.random.choice(n,n)
    s = 0.0
    for i in range(n-1):
        s += C[i+1] - C[i]
    return s/n

@jit("f8(i4)",nop
