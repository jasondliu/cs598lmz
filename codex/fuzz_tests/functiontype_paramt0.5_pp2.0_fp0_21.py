from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# TypeError: <lambda>() missing 1 required positional argument: 'x'

# The second argument is the namespace where the function's local variables
# will be looked up. In this case, the function's local variables will be
# looked up in the global namespace, which is represented by the globals()
# built-in function.

# The reason why we need to pass the globals() built-in function as the second
# argument is to make sure that the function can access the global variables
# that it needs to access.

# The function defined above is a function that takes one argument and returns
# that argument. This is a function that always returns its argument.

# This function can be used to test if a variable is defined in a namespace.

# We can test if a variable is defined in the global namespace by calling the
# function defined above and passing the variable name as the argument.

# The following is an example:

# Test if a variable is defined in the global namespace
list(FunctionType(lambda x: x, globals())('print'))

#
