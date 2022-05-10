import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(a, b):
    return a * b

# make_function takes a Python function and returns a function object
# that can be called from C
fun = make_function(FUNTYPE(f), (types.float64, types.float64))

# compile the function and get the result type and the Python callable
restype, py_fun = compile_function(fun, ())

# call the Python callable
print(py_fun(2, 3))

# call the C callable
c_fun = ctypes.cast(py_fun.c_function, FUNTYPE)
print(c_fun(2, 3))

# check the result type matches
assert(restype is types.float64)

# Compile a function with a struct return type

# define a struct type
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double)]

def make_point
