from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

def foo(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

list(foo.__code__.co_varnames)

def bar(*varargs):
    return varargs

list(bar.__code__.co_varnames)

def baz(**kwargs):
    return kwargs

list(baz.__code__.co_varnames)

def quux(arg1, arg2, *varargs, **kwargs):
    return arg1 + arg2 + varargs + kwargs

list(quux.__code__.co_varnames)
