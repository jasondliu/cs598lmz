import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap_function(lib, funcname, restype=ctypes.c_double, argtypes=[ctypes.c_double]):
    """ Simplify wrapping ctypes functions """
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

class MyLibrary(object):
    def __init__(self):
        self.lib = ctypes.CDLL('./libmylib.so')
        self.c_function = wrap_function(self.lib, 'c_function')
        self.c_function_2 = wrap_function(self.lib, 'c_function_2')


mylib = MyLibrary()
mylib.c_function(1.0)
mylib.c_function_2(1.0)
</code>

