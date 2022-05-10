import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def _make_function(function):
    return FUNTYPE(function)

def _make_callback(function):
    return FUNTYPE(function)

def _make_function_from_py_function(function):
    return FUNTYPE(function)
