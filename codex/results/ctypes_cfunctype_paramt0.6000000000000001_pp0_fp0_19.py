import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def GetProcAddress(dll, name):
    res = dll.__getattr__(name)
    res.restype = ctypes.c_void_p
    return res

def GetProcAddress_lambda(dll, name):
    return lambda: dll.__getattr__(name)

class DLLFunction:
    def __init__(self, dll, name, argtypes, restype, cfunc, doc):
        self.dll = dll
        self.name = name
        self.argtypes = argtypes
        self.restype = restype
        self.cfunc = cfunc
        self.doc = doc
        self.func = FUNTYPE(self.cfunc)
        self.func.argtypes = argtypes
        self.func.restype = restype

    def __call__(self, *args):
        return self.func(*args)

def gen_gl_func(name, argtypes, restype=None, doc=None):
    """Generate a function with the specified name and signature.
    """
   
