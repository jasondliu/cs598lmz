from types import FunctionType
list(FunctionType(lambda x: x*2, {}, None, None, None).__code__.co_varnames)

def f(a, b, c):
    return a+b*c

list(f.__code__.co_varnames)

f.__code__.co_argcount

f.__code__.co_nlocals

f.__code__.co_stacksize

f.__code__.co_flags

f.__code__.co_code

f.__code__.co_consts

f.__code__.co_names

f.__code__.co_varnames

f.__code__.co_filename

f.__code__.co_name

f.__code__.co_firstlineno

f.__code__.co_lnotab

import dis
dis.dis(f)

def f(a, b, c):
    return a+b*c

dis.dis(f)

import inspect
inspect.getsource(f)
