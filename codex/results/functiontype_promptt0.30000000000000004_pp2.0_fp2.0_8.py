import types
# Test types.FunctionType
#
# The function type is used to represent functions.
#
# The function type is an instance of the class type.
#
# The function type has the following read-only attributes:
#
# __doc__
#     The function's documentation string, or None if unavailable.
# __name__
#     The function's name.
# __dict__
#     A dictionary or other mapping object used to store the function's
#     (possibly nested) global variables. This is always a real
#     dictionary (not a subclass).
# __defaults__
#     A tuple containing default argument values for those arguments
#     that have defaults, or None if no arguments have a default value.
# __code__
#     A code object containing the compiled function body.
# __globals__
#     A reference to the dictionary that holds the function's global
#     variables -- the global namespace of the module in which the
#     function was defined. This is always a real dictionary (not a
#     subclass).
# __closure__
#     None or a tuple of cells that contain bindings for the function's
#     free variables
