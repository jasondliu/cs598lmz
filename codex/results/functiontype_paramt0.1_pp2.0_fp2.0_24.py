from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f9f8c0f5d90>, <function <lambda> at 0x7f9f8c0f5d08>]

# The first lambda is the function itself, the second is the global namespace.

# The global namespace is a dictionary, so we can use it to get the function's name:

FunctionType(lambda x: x, globals()).__name__

# '<lambda>'

# We can also use it to get the function's docstring:

FunctionType(lambda x: x, globals()).__doc__

# '<lambda>'

# We can also use it to get the function's default arguments:

FunctionType(lambda x, y=1: x, globals()).__defaults__

# (1,)

# We can also use it to get the function's annotations:

FunctionType(lambda x: x, globals()).__annotations__

# {}

# We can also use it to get the function's closure:
