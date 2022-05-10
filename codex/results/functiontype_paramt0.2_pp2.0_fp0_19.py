from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The `co_varnames` attribute is a tuple of strings, giving the names of the local variables (starting with the argument names).

# The `co_consts` attribute is a tuple containing the literals used by the bytecode.

# The `co_names` attribute is a tuple containing the names used by the bytecode.

# The `co_filename` attribute is the filename from which the code was compiled.

# The `co_firstlineno` attribute is the first line number of the function.

# The `co_lnotab` attribute is a string encoding the mapping from bytecode offsets to line numbers (for details see the compiler module).

# The `co_freevars` attribute is a tuple containing the names of free variables.

# The `co_cellvars` attribute is a tuple containing the names of local variables that are referenced by nested functions.

# The `co_stacksize` attribute is the required stack size (including local variables).

# The `co_
