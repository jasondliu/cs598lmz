import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_void_p)

def c_to_f(x, userdata):
    """
    Convert celsius to fahrenheit.
    """
    return (x * 9.0 / 5.0) + 32.0

def f_to_c(x, userdata):
    """
    Convert fahrenheit to celsius.
    """
    return (x - 32.0) * 5.0 / 9.0

def get_function(string, userdata):
    """
    Return a function pointer for the given string.
    """
    if string == "c_to_f":
        return FUNTYPE(c_to_f)
    elif string == "f_to_c":
        return FUNTYPE(f_to_c)
    else:
        return None

# get the function pointer for c_to_f
c_to_f_ptr = get_function("c_to_f", None)

# make a function that calls the function pointer
def c_to
