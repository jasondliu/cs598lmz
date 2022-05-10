from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The __code__ attribute of a function is a code object.
# A code object is a read-only object that contains the compiled bytecode for a function.
# It also contains information about the function, such as the names of the arguments and local variables.
# The co_varnames attribute of a code object is a tuple containing the names of the arguments and local variables.
# The first N elements of the tuple contain the names of the arguments in order,
# and the rest of the elements contain the names of the local variables in order.
# The number N is given by the co_argcount attribute of the code object.

# The co_varnames attribute of a code object is a tuple containing the names of the arguments and local variables.
# The first N elements of the tuple contain the names of the arguments in order,
# and the rest of the elements contain the names of the local variables in order.
# The number N is given by the co_argcount attribute of the code object.

# The co_varnames attribute
