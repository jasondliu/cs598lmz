import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def get_fib(func):
    def fib(n):
        return func(n)
    return fib

def fib1(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

def fib2(n):
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)

def fib3(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

def fib4(n):
    if n <= 2:
        return 1
    return fib4(n - 1) + fib4(n - 2)

def fib5(n):
    if n <= 2:
        return 1
    return fib5(n - 1) + fib5(n - 2)

def fib
