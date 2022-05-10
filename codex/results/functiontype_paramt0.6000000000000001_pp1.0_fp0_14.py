from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

import inspect
inspect.getargspec(lambda: None)

import dis
dis.dis(lambda: None)

# co_consts
lambda: None.__code__.co_consts

# co_names
lambda: None.__code__.co_names

# co_varnames
lambda: None.__code__.co_varnames

# co_stacksize
lambda: None.__code__.co_stacksize

# co_flags
lambda: None.__code__.co_flags

# co_lnotab
lambda: None.__code__.co_lnotab

# co_freevars
lambda: None.__code__.co_freevars

# co_cellvars
lambda: None.__code__.co_cellvars

# co_code
lambda: None.__code__.co_code

# co_firstlineno
lambda: None.__code__.co_firstlineno

# co
