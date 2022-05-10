import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def fun(x):
    return x**2

f = FUNTYPE(fun)

# f(2)

fun(2)

type(f)

%load_ext Cython
%%cython

def f(double x):
    return x ** 2

%timeit f(2)
 

%%cython

def f(double x):
    return x ** 2

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

def main():
    print(integrate_f(0, 1, 200000))

main()
%%cython

def f(double x):
    return x ** 2

cpdef double integrate_f(double a, double b, int N):
    cdef int i
   
