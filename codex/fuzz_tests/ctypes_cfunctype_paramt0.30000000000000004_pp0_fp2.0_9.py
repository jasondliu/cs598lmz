import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# define a python function
def my_func(x):
    return x**2

# convert the python function to a c function
c_func = FUNTYPE(my_func)

# call the c function
print(c_func(2))

# define a c function
c_func2 = FUNTYPE(lambda x: x**2)

# call the c function
print(c_func2(2))

# convert the c function to a python function
py_func = c_func2.__call__

# call the python function
print(py_func(2))

# define a python function
def my_func(x):
    return x**2

# convert the python function to a c function
c_func = FUNTYPE(my_func)

# call the c function
print(c_func(2))

# define a c function
c_func2 = FUNTYPE(lambda x: x**2)

# call the c function
print(c_func2(2))

