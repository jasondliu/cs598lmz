from types import FunctionType
a = (x for x in [1])
a

b = FunctionType(a.__code__, a.__globals__, a.__name__, a.__defaults__, a.__closure__)

b()

FunctionType(a.__code__, a.__globals__, a.__name__, a.__defaults__, a.__closure__)()
a.__code__.co_argcount

a.__code__.co_consts
a.__code__.co_varnames
a.__code__.co_cellvars
a.__code__.co_freevars
a.__code__.co_filename
a.__code__.co_name
a.__code__.co_nlocals
a.__code__.co_stacksize
a.__code__.co_flags
a.__code__.co_firstlineno
a.__code__.co_lnotab
a.__code__.co_names
a.__code__.co_varnames
a.gi_code

a.gi
