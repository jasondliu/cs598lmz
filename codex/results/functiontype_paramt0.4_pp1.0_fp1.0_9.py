from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# list(FunctionType(lambda: None, globals()).__code__.co_consts)

# list(FunctionType(lambda: None, globals()).__code__.co_names)

# list(FunctionType(lambda: None, globals()).__code__.co_freevars)

# list(FunctionType(lambda: None, globals()).__code__.co_cellvars)

# list(FunctionType(lambda: None, globals()).__code__.co_lnotab)

# list(FunctionType(lambda: None, globals()).__code__.co_stacksize)

# list(FunctionType(lambda: None, globals()).__code__.co_flags)

# list(FunctionType(lambda: None, globals()).__code__.co_firstlineno)

# list(FunctionType(lambda: None, globals()).__code__.co_filename)

# list(FunctionType(lambda:
