from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(2))
# [<function foo at 0x7f7f8f8c0e18>, <function foo at 0x7f7f8f8c0ea0>]

# FunctionType is a class that creates a function object.
# The first argument is a code object, and the second is a dictionary.
# The third argument is the name of the function.
# The code object is created with the built-in compile() function.

# The first argument to compile() is a string containing Python source code.
# The second argument is the filename.
# The third argument is the mode.
# The mode argument is 'exec' if the code is a statement or 'eval' if it's an expression.
# If the mode is 'exec', the code argument must be a string containing a suite of Python statements.
# If the mode is 'eval', the code argument must be a string containing a single Python expression.

# The compile() function returns a code object.
# The code object is an internal representation of the compiled code.
# It can be executed by passing it
