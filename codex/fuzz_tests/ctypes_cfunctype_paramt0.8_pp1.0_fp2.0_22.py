import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

@jit(nopython=True)
def evaluate_function(function, x):
    f = FUNTYPE(function)
    r = f(x)
    return r

@jit(nopython=True)
def f(x):
    return math.exp(x)

if __name__ == '__main__':
    evaluate_function(f, 0.2)
</code>
It takes longer to execute than the first script, and I would like to know why.

