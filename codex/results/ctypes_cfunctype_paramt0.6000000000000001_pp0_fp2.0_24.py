import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def py_function(x):
    return math.cos(x)

func = FUNTYPE(py_function)

# call the function
print(func(math.pi))

# create a function with a C function
# note that we use ctypes.c_double as the return type
def c_function(x):
    return 2*x

func = FUNTYPE(c_function)

# call the function
print(func(2))

# create a function with a lambda
func = FUNTYPE(lambda x: math.exp(x))

# call the function
print(func(1))

# create a function with a numpy function
func = FUNTYPE(np.sin)

# call the function
print(func(np.pi/2))

# create a function with a numpy ufunc
func = FUNTYPE(np.add)

# call the function
print(func(2,3))

# create a 1-dimensional array of numbers from 0 to 4
x = np.ar
