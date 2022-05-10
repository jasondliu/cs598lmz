from _struct import Struct
s = Struct.__new__(Struct)
# struct.Struct object at 0x7f4de4bd4be0
s.size = 8
Struct.__new__(Struct, 'i')
# struct.Struct object at 0x7f4de4bd4bd0

from functools import partial
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int'

from functools import update_wrapper
def decorator(d):
    '''Decorate a decorator so that it inherits the docstrings and stuff
    of functions it decorates.'''
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def my_decorator(f):
    def _f(*args, **kwargs):
        print("Decorating", f.__name__)
        return f(*args, **kwargs)
    return _f

@my_decorator
def example():
    '''Docstring'''
   
