from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The `co_varnames` attribute is a tuple of strings that contains the names of the local variables.

# The `co_argcount` attribute is the number of arguments that the function takes.

# The `co_cellvars` attribute is a tuple of strings that contains the names of the local variables that are referenced by nested functions.

# The `co_freevars` attribute is a tuple of strings that contains the names of the free variables.

# The `co_consts` attribute is a tuple of constants used by the bytecode.

# The `co_names` attribute is a tuple of strings that contains the names used by the bytecode.

# The `co_nlocals` attribute is the number of local variables used by the bytecode.

# The `co_stacksize` attribute is the required stack size.

# The `co_flags` attribute is an integer encoding a number of flags for the interpreter.

# The `co_firstlineno` attribute is the number
