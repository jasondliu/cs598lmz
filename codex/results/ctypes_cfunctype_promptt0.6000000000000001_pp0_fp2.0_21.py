import ctypes
# Test ctypes.CFUNCTYPE()

def get_address(x):
    return x.value

def get_address_ptr(x):
    return ctypes.cast(x, ctypes.c_void_p).value

def get_int(x):
    return x.value

def get_int_ptr(x):
    return ctypes.cast(x, ctypes.POINTER(ctypes.c_int)).contents.value

def get_long(x):
    return x.value

def get_long_ptr(x):
    return ctypes.cast(x, ctypes.POINTER(ctypes.c_long)).contents.value

def get_float(x):
    return x.value

def get_float_ptr(x):
    return ctypes.cast(x, ctypes.POINTER(ctypes.c_float)).contents.value

def get_double(x):
    return x.value

def get_double_ptr(x):
    return ctypes.cast(x, ctypes.POINTER(ctypes.c_double)).
