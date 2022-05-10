from types import FunctionType
list(FunctionType(func.__code__, globals(), 'func_name'))

#%%

def func(x):
    return x**2

func.__code__ = func.__code__.replace(co_consts=(1, 2, 3))

#%%

from types import CodeType
code = func.__code__
func.__code__ = CodeType(code.co_argcount,
                         code.co_kwonlyargcount,
                         code.co_nlocals,
                         code.co_stacksize,
                         code.co_flags,
                         code.co_code,
                         code.co_consts + (1, 2, 3),
                         code.co_names,
                         code.co_varnames,
                         code.co_filename,
                         code.co_name,
                         code.co_firstlineno,
                         code.co_lnotab,
                         code.co_freevars,
                         code.co_cellvars)

#%%

def func(x):
    return x**2

func.__code
