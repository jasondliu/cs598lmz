from types import FunctionType
list(FunctionType(lambda: '', {}).__code__.co_varnames)



def get_vars(f):
    return list(f.__code__.co_varnames)

def get_args(f):
    return list(f.__code__.co_varnames)[:f.__code__.co_argcount]

def get_kwargs(f):
    return list(f.__code__.co_varnames)[f.__code__.co_argcount:]

def get_defaults(f):
    return f.__defaults__

def get_defaults_dict(f):
    return dict(zip(get_kwargs(f), get_defaults(f)))

def get_arg_names(f):
    # return list(f.__code__.co_varnames)[:f.__code__.co_argcount]
    return list(f.__code__.co_varnames)[:f.__code__.co_argcount]

def get_kwarg_names(f):

