from types import FunctionType
list(FunctionType(lambda: 0, {}, '', (), None).__code__.co_freevars)

# Output:
# ['<lambda>']

# The __code__.co_freevars attribute is a tuple of strings, giving the names of
# the free variables (i.e. variables used locally, but defined in an enclosing
# scope).

# The __code__.co_cellvars attribute is a tuple of strings, giving the names of
# local variables that are referenced by nested functions.

# The __code__.co_varnames attribute is a tuple of strings, giving the names of
# the local variables (starting with the argument names).

# The __code__.co_names attribute is a tuple of strings, giving the names used
# by the bytecode. This includes the names of local variables, global variables,
# and functions referenced by the bytecode.

# The __code__.co_consts attribute is a tuple containing the literals used by
# the bytecode.

# The __code__.co_lnotab attribute is a string encoding the mapping from bytecode
#
