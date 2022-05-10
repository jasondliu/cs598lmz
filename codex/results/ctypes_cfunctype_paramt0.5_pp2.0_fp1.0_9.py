import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

# load the library, using numpy mechanisms
_lib = np.ctypeslib.load_library('_fibonacci', __file__)

# set the argument and return types
_lib.fibonacci.argtypes = (ctypes.c_int,)
_lib.fibonacci.restype = ctypes.c_int

# set the types for the callback function
_lib.fibonacci_with_callback.argtypes = (ctypes.c_int, FUNTYPE, ctypes.c_void_p)
_lib.fibonacci_with_callback.restype = ctypes.c_int


def fibonacci(n):
    """Compute the nth Fibonacci number, for n >= 0."""
    return _lib.fibonacci(n)


def fibonacci_with_callback(n, callback, data):
    """Compute the nth Fibonacci number, for
