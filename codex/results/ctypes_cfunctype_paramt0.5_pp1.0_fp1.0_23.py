import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)

def make_callback(function):
    return FUNTYPE(function)

def execute_callback(callback, argument):
    return callback(argument)

# end of file
