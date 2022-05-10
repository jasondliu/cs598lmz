from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# This is a bit of a hack, but it works.

# The function is created with a lambda, which has no arguments, so the
# co_varnames tuple will only contain the name of the lambda itself.
# Then, the __code__ attribute is accessed to get the actual code object,
# and from that, the co_varnames tuple is extracted.

# The co_varnames tuple contains the names of the arguments to the function,
# so it can be used to extract the argument names.

# The function is created with a lambda, which has no arguments, so the
# co_varnames tuple will only contain the name of the lambda itself.
# Then, the __code__ attribute is accessed to get the actual code object,
# and from that, the co_varnames tuple is extracted.

# The co_varnames tuple contains the names of the arguments to the function,
# so it can be used to extract the argument names.

# This is a bit of a hack
