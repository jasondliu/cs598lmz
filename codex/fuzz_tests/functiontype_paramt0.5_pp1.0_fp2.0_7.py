from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_consts)

# [0]

def f(): pass
f.__code__ = type(lambda: 0)(f.__code__.co_code, f.__code__.co_consts, f.__code__.co_names, f.__code__.co_varnames, f.__code__.co_filename, f.__code__.co_name, f.__code__.co_firstlineno, f.__code__.co_lnotab, f.__code__.co_freevars, f.__code__.co_cellvars)

list(f.__code__.co_consts)
# [0]

f.__code__.co_consts = (0, 1, 2, 3)
list(f.__code__.co_consts)
# [0, 1, 2, 3]

# f.__code__.co_consts = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
