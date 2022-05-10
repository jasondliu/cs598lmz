import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_func(f):
    return FUNTYPE(f)

def make_func_ptr(f):
    return ctypes.cast(make_func(f), ctypes.c_void_p).value

def make_func_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(make_func(f)), ctypes.c_void_p).value

def make_func_ptr_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(ctypes.pointer(make_func(f))), ctypes.c_void_p).value

def make_func_ptr_ptr_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(ctypes.pointer(ctypes.pointer(make_func(f)))), ctypes.c_void_p).value

def make_func_ptr_ptr_ptr_ptr_ptr(f):
    return ctypes.cast(ctypes.pointer(ctypes.pointer(ctypes.
