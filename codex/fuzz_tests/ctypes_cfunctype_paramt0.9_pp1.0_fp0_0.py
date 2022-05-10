import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                          ctypes.c_double,
                          ctypes.c_double)
def create_function(python_function):
    python_function.restype = ctypes.c_double
    python_function.argtypes = [ctypes.c_double,
                                ctypes.c_double]
    return python_function

def print_error(err):
    print ("Error: %g" % err)

def print_integral(result, err):
    print ("Integral = %g +/- %g" % (result, err))

def my_function(x,y):
    return x * y * x * y * x * y * x * y

def main():
    func_ptr = create_func
