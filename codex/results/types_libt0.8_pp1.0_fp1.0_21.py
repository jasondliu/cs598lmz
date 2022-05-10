import types
types.FunctionType

# The builtin functions
import __builtin__
__builtin__.range

# The standard library functions
from statistics import mean
mean

# The dir function shows the attributes of an object
dir(mean)

# help displays the doc string of a function
help(mean)

# The first positional argument of a function can be referenced by name
mean([1,2,3], 0) == mean(iterable=[1,2,3], axis=0)

# Many functions have a flexible number of positional arguments
def flexible_args(*args):
    return args

flexible_args(1, 2, 3, 4, 5)

# Many functions have a flexible number of keyword arguments
def flexible_kwargs(**kwargs):
    return kwargs

flexible_kwargs(x=1, y=2)

# A function definition can include both types of flexible arguments
def flexible_args_kwargs(*args, **kwargs):
    print "Positional arguments:", args
    print "Keyword arguments:", kwargs

flexible_args_kw
