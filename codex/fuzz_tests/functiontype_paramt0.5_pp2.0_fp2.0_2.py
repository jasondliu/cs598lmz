from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__).__code__.co_varnames)

from types import CodeType
list(CodeType(f.__code__.co_argcount, f.__code__.co_kwonlyargcount, f.__code__.co_nlocals, f.__code__.co_stacksize, f.__code__.co_flags, f.__code__.co_code, f.__code__.co_consts, f.__code__.co_names, f.__code__.co_varnames, f.__code__.co_filename, f.__code__.co_name, f.__code__.co_firstlineno, f.__code__.co_lnotab, f.__code__.co_freevars, f.__code__.co_cellvars).co_varnames)

from types import CodeType
CodeType(f.__code__.co_argcount, f.
