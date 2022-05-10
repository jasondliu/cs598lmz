import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print(f_c(2))

print(f_c(3))

print(f_c(4))

print(f_c(5))

print(f_c(6))

print(f_c(7))

print(f_c(8))

print(f_c(9))

print(f_c(10))

print(f_c(11))

print(f_c(12))

print(f_c(13))

print(f_c(14))

print(f_c(15))

print(f_c(16))

print(f_c(17))

print(f_c(18))

print(f_c(19))

print(f_c(20))

print(f_c(21))

print(f_c(22))

print(f_c
