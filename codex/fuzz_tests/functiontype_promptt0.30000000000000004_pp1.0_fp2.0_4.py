import types
# Test types.FunctionType
#
# This type is used to represent a function.  The only operations
# understood by this type are attribute access and call.  In order to
# call a function, it must be passed at least one argument.  In order
# to access an attribute of a function, the attribute name must be a
# string.  Attempting to access an attribute of a function whose name
# is not a string will raise a TypeError exception.
#
# The following attributes are defined for function objects:
#
# __doc__         The documentation string of the function, or None if
#                 undefined.
#
# __name__        The name of the function.
#
# __self__        For bound methods, this is the object on which the
#                 method operates; for unbound methods, this is None.
#
# __dict__        A dictionary or other mapping object used to store a
#                 function's (or other callable's) attributes.
#
# __code__        A code object containing the compiled function body.
#
# __defaults__    A tuple containing default argument values for those
#                 arguments that have defaults, or
