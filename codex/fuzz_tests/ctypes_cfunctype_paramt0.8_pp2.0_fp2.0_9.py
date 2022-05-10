import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, POINTER(ctypes.c_double))

def set_to_array(func):
    @wraps(func)
    def wrapper(self, *args):
        return self.array(func(self, *args))
    return wrapper

def set_to_array0(func):
    @wraps(func)
    def wrapper(self, *args):
        return self.array(func(self))
    return wrapper

def c_to_array(func):
    @wraps(func)
    def wrapper(self, *args):
        return self.c_array(func(self, *args))
    return wrapper

def c_to_array0(func):
    @wraps(func)
    def wrapper(self, *args):
        return self.c_array(func(self))
    return wrapper

def c_to_array0v2(func):
    @wraps(func)
    def wrapper(self, *args):
        return self.c_array(func(self, self[ci.V
