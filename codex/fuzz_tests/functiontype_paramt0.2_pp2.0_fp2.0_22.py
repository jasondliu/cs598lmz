from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f') for f in [lambda x: x+1, lambda x: x+2])

# [<function <lambda> at 0x7f8f7c1a2f28>, <function <lambda> at 0x7f8f7c1a2ea0>]

# The first argument to FunctionType is the code object.
# The second argument is the global namespace.
# The third argument is the name of the function.

# The code object is the compiled version of the function body.
# It contains the bytecode instructions of the function body,
# the constants that are referenced in the function body,
# information about the local variables and free variables of the function,
# and the names of the arguments.

# The global namespace is the namespace in which the function body is executed.
# This is the namespace in which the function body is compiled.

# The name of the function is the name of the function as seen by the code object.
# It is not necessarily the same as the name of the variable in which the function is stored.

# The function object is created by
