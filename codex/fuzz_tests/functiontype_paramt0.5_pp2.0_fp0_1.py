from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['None']

# The __code__ object also contains a co_consts tuple containing the constants used in the bytecode.
# The co_consts tuple contains the literals used by the bytecode
# (e.g., strings, numbers, and tuples), as well as references to code objects for nested functions and
# classes.

# The co_names attribute is a tuple containing the names used by the bytecode.
# It includes all local variables, global variables, and built-in names that are referenced by the code.

# The co_varnames attribute is a tuple containing the names of the local variables
# (excluding arguments).

# The co_freevars attribute is a tuple containing the names of free variables.
# A free variable is a variable that is referenced in the nested function but not defined in it.
# Free variables are looked up in the scope surrounding the definition of the nested function.

# The co_cellvars attribute is a tuple containing the names of local variables that are referenced by nested functions.

# The co_cell
