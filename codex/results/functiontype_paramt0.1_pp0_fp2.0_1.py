from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f9d9c9d3f28>, <function <lambda> at 0x7f9d9c9d3ea0>]

# The second argument to FunctionType is the globals dictionary.
# This is used to resolve any global variables that the function references.
# If you don't pass in a globals dictionary, the function will not be able to
# reference any global variables.

# The first argument to FunctionType is a code object.
# This is the compiled bytecode for the function body.
# The code object is the same thing returned by the built-in compile function.

# The code object is the most important argument to FunctionType.
# It is the compiled bytecode for the function body.
# The code object is the same thing returned by the built-in compile function.

# The code object is the most important argument to FunctionType.
# It is the compiled bytecode for the function body.
# The code object is the same thing returned by the built-in compile function.

# The code object is the
