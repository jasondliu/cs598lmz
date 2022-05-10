import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def c_function(f):
    return FUNTYPE(f)

def c_function_pointer(f):
    return ctypes.cast(c_function(f), ctypes.c_void_p).value

def c_function_pointer_to_int(f):
    return ctypes.cast(c_function(f), ctypes.c_int).value

def c_function_pointer_to_long(f):
    return ctypes.cast(c_function(f), ctypes.c_long).value

def c_function_pointer_to_void_p(f):
    return ctypes.cast(c_function(f), ctypes.c_void_p).value

def c_function_pointer_to_c_char_p(f):
    return ctypes.cast(c_function(f), ctypes.c_char_p).value

def c_function_pointer_to_c_void_p(f):
    return ctypes
