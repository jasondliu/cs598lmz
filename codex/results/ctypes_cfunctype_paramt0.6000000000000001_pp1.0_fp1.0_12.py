import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
def my_f(x):
    return 2.0*x
my_f_c = FUNTYPE(my_f)
my_f_c(2.0)

# Callback function with arguments
# http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#callback-functions-with-arguments

# Define the callback function
def f(x, a, b, c):
    return a*x**2 + b*x + c

# Convert the Python function to a C function
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)
f_c = FUNTYPE(f)

# Define the C function as an external function
def f_external(x, a, b, c):
    return f_c(x, a, b, c)

# Create the callback function
def f_
