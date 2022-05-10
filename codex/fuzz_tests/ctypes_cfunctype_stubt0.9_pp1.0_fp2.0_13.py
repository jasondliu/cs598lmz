import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
print(fun)
print(fun.__code__.co_argcount)
print(fun.__code__.co_varnames)
print(fun.__code__.co_argcount, fun.__code__.co_varnames)


print("function has code object")

#compile(co_code, co_name, co_filename, co_firstline, co_lnotab, co_stacksize, co_flags, co_consts, co_names, co_varnames, co_filename, co_name, co_firstlineno, co_argcount, co_kwonlyargcount, co_nlocals, co_cellvars, co_freevars)  
#compile(code, filename, mode, flags=0, dont_inherit=False)

import types
def fun_checker(fun, funname):
    return isinstance(fun,types.FunctionType) and fun.__name__==funname and fun.__code__.co_argcount==0
