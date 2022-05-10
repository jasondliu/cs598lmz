import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_int) #Obtains
                                                        # function type
                                                        # argument types from
                                                        # function argument
                                                        # types and return
                                                        # type
def test_function(i):
    return i+4

function_type = FUNTYPE(test_function)

f = function_type(test_function)

assert f(4) == 8
</code>

