import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def get_int(x):
    return x.value

def set_int(x, val):
    x.value = val

def get_float(x):
    return x.value

def set_float(x, val):
    x.value = val

def get_null(x):
    return x.value

def set_null(x, val):
    x.value = val

def get_bool(x):
    return x.value

def set_bool(x, val):
    x.value = val

def get_string(x):
    return x.value

def set_string(x, val):
    x.value = val

def get_array(x):
    return x.value

def set_array(x, val):
    x.value = val

def get_dict(x):
    return x.value

def set_
