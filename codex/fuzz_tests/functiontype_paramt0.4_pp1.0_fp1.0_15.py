from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# f.__closure__ is None
# f.__defaults__ is None

# f.__code__
# f.__code__.co_varnames
# f.__code__.co_argcount

# f.__code__.co_code
# f.__code__.co_consts
# f.__code__.co_names
# f.__code__.co_nlocals
# f.__code__.co_flags
# f.__code__.co_freevars
# f.__code__.co_cellvars

# f.__code__.co_consts
# f.__code__.co_names

# f.__code__.co_code
# f.__code__.co_code
# f.__code__.co_code
# f.__code__.co_code

# f.__code__.co_code
# f
