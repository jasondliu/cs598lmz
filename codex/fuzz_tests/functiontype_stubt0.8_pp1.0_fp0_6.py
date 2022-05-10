from types import FunctionType
a = (x for x in [1])
type(a), a.gi_frame.f_locals

a = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals)
a()

a = list(a())  # a generator function is returned
a

def f(x):
    y = yield x
    return y + 2

a = f(2)
type(a), a.gi_frame.f_locals

a = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals)
a()

next(a())  # the iteration will be started

a, next(a())

try:
    next(a())
except StopIteration as e:
    a, e.value

a = list(a())  # a generator function is returned
a
 
%%time
from types import GeneratorType as Generator
from types import FunctionType

def f(x):
    yield x
    g = (yield from f(x + 1))
    return g + x

a =
