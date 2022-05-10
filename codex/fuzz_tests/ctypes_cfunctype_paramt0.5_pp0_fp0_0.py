import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def wrap_function(lib, name):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(name)
    func.argtypes = (ctypes.c_double,)
    func.restype = ctypes.c_double
    return func

class MyFunc:
    """This is a class that wraps a C function and makes it callable"""
    def __init__(self, lib, name):
        self.func = wrap_function(lib, name)
    def __call__(self, x):
        return self.func(x)

if __name__ == "__main__":
    # load the shared library into ctypes
    mylib = ctypes.cdll.LoadLibrary("./mylib.so")

    # wrap the cos and sin functions
    cos_func = wrap_function(mylib, "cos")
    sin_func = wrap_function(mylib, "sin")

    # test the cos function
    print("cos(2) = ", cos_
