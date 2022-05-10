from types import FunctionType
list(FunctionType(lambda x: x, {}, 'f').__code__.co_cellvars)

# list(FunctionType(lambda x: x, {}, 'f').__code__.co_freevars)

# list(FunctionType(lambda x: x, {}, 'f').__code__.co_varnames)

# list(FunctionType(lambda x: x, {}, 'f').__code__.co_names)

# list(FunctionType(lambda x: x, {}, 'f').__code__.co_consts)

# list(FunctionType(lambda x: x, {}, 'f').__code__.co_lnotab)

# FunctionType(lambda x: x, {}, 'f').__code__.co_stacksize

# FunctionType(lambda x: x, {}, 'f').__code__.co_flags

# FunctionType(lambda x: x, {}, 'f').__code__.co_argcount

# FunctionType(lambda x: x, {}, 'f').__code__.co_kwonlyargcount
