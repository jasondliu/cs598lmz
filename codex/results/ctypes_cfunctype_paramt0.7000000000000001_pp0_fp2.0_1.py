import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double))

class Functor(object):
    def __init__(self, fun):
        self.fun = FUNTYPE(fun)

def func(i):
    def func(n, x):
        return x[n-1]
    return Functor(func)

def fib(i):
    def fib(n, x):
        if n &gt; 1:
            return x[n-2] + x[n-1]
        else:
            return 1
    return Functor(fib)

def main(n):
    N = n
    x = (ctypes.c_double*N)()

    fun = fib(0)
    f = fun.fun
    for i in range(n):
        x[i] = f(i,x)
    print x[-1]

main(10)
</code>
Output:
<code>89
</code>

