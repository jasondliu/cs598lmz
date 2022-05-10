from types import FunctionType
list(FunctionType(f.func_code, f.func_globals))

def is_function(x):
    return isinstance(x, FunctionType)

def is_function_old(x):
    return isinstance(x, types.FunctionType) or isinstance(x, types.LambdaType)

def is_string(x):
    if isinstance(x, basestring):
        return True
    if isinstance(x, str):
        return True
    return False

def is_integer(x):
    return isinstance(x, int)

def is_float(x):
    return isinstance(x, float)

def is_number(x):
    return is_integer(x) or is_float(x)

def is_list(x):
    return isinstance(x, list)

def is_tuple(x):
    return isinstance(x, tuple)

def is_sequence(x):
    return is_list(x) or is_tuple(x)

def is_dict(x):
    return is
