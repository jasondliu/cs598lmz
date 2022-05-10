import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
# Define a C callback for the C library
@FUNTYPE
def c_f(x):
    return np.exp(-(x**2))

# Call the C library function with the C callback
c_integral = c_quadrature(c_f, 0.0, 1.0, 100)
print('C library result:', c_integral)

# Define a Python callback for the C library
@FUNTYPE
def py_f(x):
    return np.exp(-(x**2))

# Call the C library function with the Python callback
py_integral = c_quadrature(py_f, 0.0, 1.0, 100)
print('C library result:', py_integral)
 
 
 

# C library function prototype
# double c_quadrature(double (*f)(double), double a, double b, int n)
#
# double f(double x) {
#    return exp(-x*x);
# }
#
# int main()
