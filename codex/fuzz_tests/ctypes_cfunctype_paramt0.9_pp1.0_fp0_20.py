import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
class foofunc:
    def __init__(self,fun):
        self._fun=fun
    def __call__(self,x):
        return self._fun(x)
    def __getattr__(self,attr):
       return getattr(self._fun,attr)

restype=ctypes.c_double

def wrap(fun,argtype,restype,asCFunc = True,default = 0.0):
    """wrap(fun,argtype,restype) wraps
    c function taking args of type argtype
    returning type restype into a python
    function. If asCFunc is True, returns
    an object that can be
    treated like a cfunc.
    """
    fun.restype = restype
    fun.argtypes = [argtype]
    def call(x):
        return fun(x)
    if asCFunc:
        fun = CFunc(fun,default)
    return fun


if __name__ == "__main__":
    import pylab
