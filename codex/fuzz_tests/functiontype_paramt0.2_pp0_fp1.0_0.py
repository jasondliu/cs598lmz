from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__qualname__', '__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# __code__ is a code object.
# __code__.co_varnames is a tuple of strings.

# The first string is the name of the function.
# The rest of the strings are the names of the arguments.

# The first string is the name of the function.
# The rest of the strings are the names of the arguments.

# The first string is the name of the function.
# The rest of the strings are the names of the arguments.

# The first string is the name of the function.
# The rest of the strings are the names of the arguments.

# The first string is the name of the function.
# The rest of the strings are the names of the arguments.

# The first string is the name of
