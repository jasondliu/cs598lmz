import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, p_int, p_double)
# function to be called
def func(x, y):
    y[0] = 2 * x[0]
    return 0
CFUNC = FUNTYPE(func)

def sample_callback(X):
    return CFUNC(X.ctypes.data_as(p_int),
                 X.ctypes.data_as(p_double))

# create a 10-dimensional vector
x = np.arange(10, dtype=np.int32)
print(x)
# call the sample callback function
sample_callback(x)
print(x)

#======================= another example ======================
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, p_int, p_double)
# function to be called
def func(x, y):
    y[0] = 2 * x[0].value
    return 0
CFUNC = FUNTYPE(func)
def sample_callback(x):
    return CFUNC(x.ctypes
