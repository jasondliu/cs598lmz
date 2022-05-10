import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, c_double, c_double)
free_callbacks = []
def create_generic_callbackfunction(pythonfunction, number_of_parameters=2):
    from ctypes import c_void_p
    from .util import convert2CFunction

    function = create_functionpointer(pythonfunction)
    argtypes = (c_void_p, c_void_p) * number_of_parameters
    cfunction = convert2CFunction(function, argtypes)
    # FIXME: this crashes
    #free_callbacks.append(cfunction)
    return cfunction


def create_functionpointer(f):
    """
    Create a ctypes CFUNCTYPE callback function. This function can be passed to
    a functionpointer in a shared library
    """
    from ctypes import CFUNCTYPE, c_void_p, c_int, c_double
    pointer = CFUNCTYPE(c_void_p, c_int, c_void_p, c_double)(f)
    free_callbacks.append(pointer)
    return pointer


