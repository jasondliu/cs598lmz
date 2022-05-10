import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float,ctypes.c_float)

# define a python function
def python_func(x):
    return x*x

# convert python function to c function
c_func = FUNTYPE(python_func)

# call the c function
print c_func(5.0)
</code>
This seems to work, but I'm not sure if this is the "correct" way to do it. 

