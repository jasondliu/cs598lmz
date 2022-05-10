import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def gen_callback(f):
    def wrapper(x, y, z, w, v):
        f(x, y, list(z), list(w), list(v))
    return FUNTYPE(wrapper)

# Wraps the C library function
def C_wrapper(func, *args, **kwargs):
    func.restype = None
    if 'callback' in kwargs:
        f = kwargs.pop('callback')
        kwargs['callback'] = gen_callback(f)
    return func(*args, **kwargs)

# Wraps the Python function
def Python_wrapper(func, *args, **kwargs):
    if 'callback' in kwargs:
        f = kwargs.pop('callback')
        def wrapper(x, y, z, w, v):
            f(x,
