import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_int,ctypes.c_double,ctypes.c_double)

#https://stackoverflow.com/questions/8671808/how-do-i-pass-a-function-as-a-parameter-in-python/8671849

def matrix_power(n):
    M = np.array([[1,1],[1,0]])
    return (M**n)

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2

