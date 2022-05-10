from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

# FunctionType(code, globals[, name[, argdefs[, closure]]])

# Create a function with a given name and code, and global namespace globals.
#
# code must be a compiled code object (see compile()). The optional name
# string overrides the name from the code object. The optional argdefs argument
# specifies the default argument values for those parameters which have
# defaults, otherwise None. The optional closure argument must be a tuple
# containing the bindings for free variables.
#
# The resulting function has the same restrictions on argument lists as
# functions created with the def statement.

# Return a new function object.
#
# The code object must be a compiled function (see compile()). The
# globals must be a dictionary and provide the global namespace for
# the function. The name string is the name of the function. The
# argdefs tuple specifies the default argument values. The closure tuple
# must
