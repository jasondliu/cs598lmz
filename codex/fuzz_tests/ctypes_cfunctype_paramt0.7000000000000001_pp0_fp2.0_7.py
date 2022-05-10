import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Can use this function to check if a number is a float
def _isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def _get_float_from_str(string):
    try:
        return float(string)
    except ValueError:
        return None

def _get_operator(string):
    try:
        return OPERATORS[string]
    except KeyError:
        return None

def _get_function(string):
    try:
        return FUNCTIONS[string]
    except KeyError:
        return None

def _get_function_args(string):
    try:
        return FUNCTION_ARGS[string]
    except KeyError:
        return None

def _create_function(function, args):
    return FUNTYPE(function(args))

def _get_variable(string):
    try:
        return VARIABLES[string]
    except KeyError:
       
