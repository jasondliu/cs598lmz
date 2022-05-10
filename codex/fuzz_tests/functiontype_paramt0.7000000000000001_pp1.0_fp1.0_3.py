from types import FunctionType
list(FunctionType().__dict__)

import pprint
pprint.pprint(globals()['__builtins__'].__dict__)
# pprint.pprint(globals().__dict__)

import inspect

def get_args(func):
    """Get arguments of a function."""
    args, varargs, keywords, defaults = inspect.getargspec(func)
    return args

def get_defaults(func):
    """Get defaults of a function."""
    args, varargs, keywords, defaults = inspect.getargspec(func)
    if defaults is None:
        defaults = ()
    return defaults

def get_kwargs(func):
    """Get keyword arguments of a function."""
    func_args = get_args(func)
    defaults = get_defaults(func)
    kwargs = dict(zip(func_args[-len(defaults):], defaults))
    return kwargs

get_args(lambda a, b=1, c=2: None)
# ['a', 'b', 'c']

get_
