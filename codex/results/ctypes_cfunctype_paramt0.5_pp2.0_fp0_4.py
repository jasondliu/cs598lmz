import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(x):
    return x % 2

c_func = FUNTYPE(py_func)

@jit(nopython=True)
def nb_func(x):
    return x % 2

def time_func(func, runs=1000):
    start = time.time()
    for i in range(runs):
        func(i)
    return (time.time() - start) / runs

py_time = time_func(py_func)
c_time = time_func(c_func)
nb_time = time_func(nb_func)

print(f"Python: {py_time:.2e}s")
print(f"C: {c_time:.2e}s")
print(f"Numba: {nb_time:.2e}s")

print(f"Numba is {py_time / nb_time:.2f}x faster than pure Python")
print(f"Numba is {c
