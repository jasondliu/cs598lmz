import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# Generate a C string containing the C code that defines the C function as a python ctypes function
Cfunction = """
double function(double x, double y) {
    return sin(x*log(y));
}
"""

# Generate a ctypes function from the c function
Cfunction = CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)('function')

# Create a dictionary of variables (the inputs)
variables = {}
variables['x'] = 2
variables['y'] = 2

# Evaluate the function
print evaluate(variables, Cfunction)
