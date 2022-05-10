import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(f):
    return FUNTYPE(f)

def make_function_ptr(f):
    return ctypes.cast(make_function(f), ctypes.c_void_p).value

def make_function_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(make_function(f)), ctypes.c_void_p).value

def make_function_ptr_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(ctypes.pointer(make_function(f))), ctypes.c_void_p).value

def make_function_ptr_ptr_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(ctypes.pointer(ctypes.pointer(make_function(f)))), ctypes.c_void_p).value

def make_function_ptr_ptr_ptr_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(ctypes.pointer(ctypes.
