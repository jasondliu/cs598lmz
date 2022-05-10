import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def use_cfunc_16(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        newargs = tuple(16 if isinstance(x, _Type) else x for x in args)
        return f(*newargs, **kwds)
    return wrapper

class Test:
    def __call__(self, x):
        return x

class NewBase:
    @use_cfunc_16
    def __new__(cls,*args):
        instance = super(NewBase, cls).__new__(cls,*args)
        return instance

    def __init__(self):
        self.__dict__ = {'d': 0}    
    def __setattr__(self, name, val):
        if name == "d":
            self.__dict__['d'] = val
        else:
            self.__dict__[name] = val

    def __call__(self, x):
        return x
        
def _test1
