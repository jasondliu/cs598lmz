import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                          ctypes.c_double, ctypes.c_double, ctypes.c_double,
                          ctypes.c_double, ctypes.c_double)

def create_c_function(function):
    return FUNTYPE(function)

def create_python_function(function):
    def pyfunc(x, y, z, t, s):
        return function(x, y, z, t, s)
    return pyfunc

def create_c_function_from_python(function):
    return create_c_function(create_python_function(function))

def create_python_function_from_c(function):
    return create_python_function(create_c_function(function))

# Define a Python function
def my_function(x, y, z, t, s):
    return x * y * z * t * s
# Convert to a C function
my_c_function = create_c_function(my_function)
# Call the C function
my_c_function(1.0,
