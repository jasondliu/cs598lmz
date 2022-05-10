import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def compute(n, f, a, b, pool):
    h = (b-a)/n
    result = 0.0
    for i in range(n):
        result += f(a + (i+0.5)*h)
    return h*result

def compute_with_pool(f, a, b, *args, **kwargs):
    pool = Pool(*args, **kwargs)
    result = 0.0
    for _, res in pool.imap_unordered(partial(compute, f=f, a=a, b=b),
            pool.map(repeat, range(1, pool._processes+1)), chunksize=1):
        result += res
    return pool.terminate(), result

def run(argv):
    print(compute_with_pool(FUNTYPE(lambda x: x*x*x)(), 0, 3))
    print(compute_with_pool(lambda x: x*x*x, 0, 3, 4))

if __
