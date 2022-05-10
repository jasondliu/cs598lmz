import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# load the shared library into ctypes
lib = ctypes.CDLL("./libfoo.so")

# define the function prototype
lib.foo.argtypes = [ctypes.c_int]
lib.foo.restype = ctypes.c_int

# call the function
print(lib.foo(5))

# define the function prototype
lib.foo.argtypes = [ctypes.c_int, FUNTYPE]
lib.foo.restype = ctypes.c_int

# define the callback
def my_callback(a):
    print("my_callback called with {}".format(a))
    return a

# call the function
print(lib.foo(5, FUNTYPE(my_callback)))

# define the function prototype
lib.foo.argtypes = [ctypes.c_int, FUNTYPE]
lib.foo.restype = ctypes.c_int

# define the callback
def my_callback(a):
    print("my_callback called with {}".format(a
