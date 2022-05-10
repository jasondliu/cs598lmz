fn = lambda: None
# Test fn.__code__ for CPython only
def get_code(fn):
    return fn.__code__

# Test fn.__name__ for CPython only
def get_name(fn):
    return fn.__name__

# Test fn.__defaults__ for CPython only
def get_defaults(fn):
    return fn.__defaults__

def get_argcount(fn):
    return fn.__code__.co_argcount

def get_nlocals(fn):
    return fn.__code__.co_nlocals

def get_varnames(fn):
    return fn.__code__.co_varnames

def call_function(fn, args):
    return fn(*args)

def call_function_with_kwargs(fn, args, kwargs):
    return fn(*args, **kwargs)

def call_function_with_kwargs_and_starargs(fn, args, kwargs, starargs):
    return fn(*args, **kwargs, *starargs)

def call_function_with_
