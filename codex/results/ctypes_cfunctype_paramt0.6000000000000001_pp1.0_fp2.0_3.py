import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_c_fun(func):
    return FUNTYPE(func)

def integrate(f, a, b, n):
    h = (b-a)/float(n)
    I = 0
    for i in range(n):
        I += f(a+i*h)
    return I * h

# This is the function we want to integrate
def f(x):
    return x**2

# Get a ctypes pointer to the function
c_f = get_c_fun(f)

# Integrate the function
integrate(c_f, 0, 1, 100)

# It's easy to call the function directly
c_f(1)

# It's also easy to call the function using the Python function object
f(1)
 
 

# Define a Python function to be used in C
def f_py(x):
    return x**2

# Define a C function to be used in Python
def f_c(x):
    return x**
