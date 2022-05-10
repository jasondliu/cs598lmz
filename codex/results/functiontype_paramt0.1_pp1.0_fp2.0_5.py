from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y']

# The __code__ attribute of a function is a code object.
# The co_varnames attribute of a code object is a tuple of strings.
# The strings are the names of the local variables used by the function.
# The first string is the name of the argument, and the rest are the names of the local variables.

# The __code__ attribute of a function is a code object.
# The co_varnames attribute of a code object is a tuple of strings.
# The strings are the names of the local variables used by the function.
# The first string is the name of the argument, and the rest are the names of the local variables.

# The __code__ attribute of a function is a code object.
# The co_varnames attribute of a code object is a tuple of strings.
# The strings are the names of the local variables used by the function.
# The first string is the name of the argument, and the rest are the names of the local variables.

# The __code__ attribute
