from types import FunctionType
list(FunctionType(None, None, None, None).__code__.co_varnames)

def f(a, b, c):
    return a + b + c
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)
print(f.__code__.co_argcount)
print(f.__code__.co_nlocals)
print(f.__code__.co_stacksize)
print(f.__code__.co_flags)
print(f.__code__.co_consts)
print(f.__code__.co_names)
print(f.__code__.co_varnames)
print(f.__code__.co_cellvars)
print(f.__code__.co_freevars)
print(f.__code__.co_filename)
print(f.__code__.co_name)
print(f.__code__.co_firstlineno)
print(f.__code__.co_lnotab)

def f
