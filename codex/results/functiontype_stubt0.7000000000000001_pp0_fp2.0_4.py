from types import FunctionType
a = (x for x in [1])
type(a)

FunctionType

dir(a)

a.gi_frame.f_code.co_name

def foo(a, b):
    return a + b
foo.__name__

a.gi_frame.f_code.co_name

a.gi_frame.f_code.co_filename

a.gi_frame.f_code.co_firstlineno

def foo(a, b): return a + b
foo.__name__

foo.__code__.co_name

foo.__code__.co_filename

foo.__code__.co_firstlineno

a.gi_frame.f_code.co_varnames

a.gi_frame.f_code.co_argcount

a.gi_frame.f_code.co_flags

from inspect import getargspec
getargspec(foo)

from inspect import getargspec
def foo(a, b, c=1, d=0, *args, **kwargs):
    pass
getargspec(foo
