from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f9b3a3f5e18>, <function <lambda> at 0x7f9b3a3f5ea0>]

# The first is the lambda itself, the second is the globals() function.

# The second argument to FunctionType can be any mapping, but it must contain the __builtins__ key.

# The third argument is the name of the function, which defaults to <lambda>.

# The fourth argument is the docstring of the function, which defaults to None.

# The fifth argument is the number of arguments the function takes, which defaults to the number of arguments in the lambda.

# The sixth argument is the default values of the arguments, which defaults to an empty tuple.

# The seventh argument is the closure of the function, which defaults to an empty tuple.

# The eighth argument is the namespace of the function, which defaults to an empty mapping.

# The ninth argument is the flag that indicates whether the function is a generator, which defaults to False.

# The tenth argument is the flag that
