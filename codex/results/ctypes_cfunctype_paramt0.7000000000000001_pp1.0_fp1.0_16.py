import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
def py_dif(x):
    return x**2-2*x
def py_fun(x):
    return x**3/3-x**2+x

func = FUNTYPE(py_dif)
integrate = FUNTYPE(py_fun)

a = 0
b = 4
step = 1e-3

integral = integrate_func(func, a, b, step)
print(integral)

#integral_test = integrate_func_test(func, a, b, step)
#print(integral_test)

integral_omp = integrate_func_omp(func, a, b, step)
print(integral_omp)

integral_omp_test = integrate_func_omp_test(func, a, b, step)
print(integral_omp_test)

integral_omp_test_2 = integrate_func_omp_test_2(func, a, b, step)
print(integral_omp_test_2)


