import ctypes
# Test ctypes.CFUNCTYPE

def get_callback(f):
    if not isinstance(f, type(get_callback)):
        f = get_callback(f)
    return f

def get_callback_class(f):
    if not isinstance(f, type(get_callback_class)):
        f = get_callback_class(f)
    return f

def get_callback_instance(f):
    if not isinstance(f, type(get_callback_class)):
        f = get_callback_instance(f)
    return f

