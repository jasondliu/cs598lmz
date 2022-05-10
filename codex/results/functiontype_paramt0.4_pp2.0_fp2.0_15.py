from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'addone')(i) for i in range(4))

# ------------------------------------------------------------------------------
# FunctionType.__code__
# ------------------------------------------------------------------------------

# FunctionType.__code__ is a read-only attribute that returns the code object
# associated with the function.

# ------------------------------------------------------------------------------
# FunctionType.__defaults__
# ------------------------------------------------------------------------------

# FunctionType.__defaults__ is a read-only attribute that returns a tuple
# containing default argument values for those arguments that have defaults, or
# None if no arguments have a default value.

# ------------------------------------------------------------------------------
# FunctionType.__dict__
# ------------------------------------------------------------------------------

# FunctionType.__dict__ is a read-only attribute that returns the dictionary
# containing the function's namespace.

# ------------------------------------------------------------------------------
# FunctionType.__doc__
# ------------------------------------------------------------------------------

# FunctionType.__doc__ is a read-only attribute that returns the function's
# documentation string, or None if undefined.

# ------------------------------------------------------------------------------
# FunctionType.__globals__
# ------------------------------------------------------------------------------

# FunctionType.__globals__ is a read
