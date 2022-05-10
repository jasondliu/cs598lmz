from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# list(FunctionType(lambda: None, {}).__code__.co_freevars)

# from types import FunctionType
# list(FunctionType(lambda: None, {}).__code__.co_cellvars)

# from types import FunctionType
# list(FunctionType(lambda: None, {}).__code__.co_names)


# from types import FunctionType
# list(FunctionType(lambda: None, {}).__code__.co_consts)


# import sys
# sys.flags

# from types import FunctionType
# FunctionType(lambda: None, {}).__code__.co_flags


# from types import FunctionType
# FunctionType(lambda: None, {}).__code__.co_firstlineno

# from types import FunctionType
# FunctionType(lambda: None, {}).__code__.co_lnotab

# from types import FunctionType
# FunctionType(lambda: None, {}).__code__.co_stacksize


# import sys
