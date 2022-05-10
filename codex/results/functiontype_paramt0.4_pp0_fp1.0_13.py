from types import FunctionType
list(FunctionType(lambda: 1, globals(), 'foo'))

# __doc__
# __name__
# __qualname__
# __module__
# __defaults__
# __code__
# __globals__
# __closure__
# __annotations__
# __kwdefaults__

# FunctionType(code, globals, name, argdefs, closure)

# code:
#   The compiled code object (see below)
# globals:
#   The global namespace in which the function should be defined
# name:
#   The name of the function
# argdefs:
#   The default argument values (None if no default arguments)
# closure:
#   The closure for the function (None if no closure)

# The code object is a compiled version of the function’s body.
# It is the object returned by the built-in compile() function.
# The code object can be created from a string containing Python source code
# (see the built-in compile() function for details) or from a Python AST object
# (see the compiler package for details).

# The
