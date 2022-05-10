import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(name, address):
    return FUNTYPE(address)(name)

def make_function_from_c_function(name, c_function):
    return make_function(name, ctypes.addressof(c_function))

def make_function_from_c_function_pointer(name, c_function_pointer):
    return make_function(name, ctypes.cast(c_function_pointer, ctypes.c_void_p).value)

def make_function_from_c_function_pointer_with_type(name, c_function_pointer, c_function_type):
    return make_function(name, ctypes.cast(c_function_pointer, ctypes.POINTER(c_function_type)).contents.value)

def make_function_from_c_function_pointer_with_type_and_argtypes(name, c_function_pointer, c_function_type, argtypes):
    return make_function(name, ctypes.cast(c_
