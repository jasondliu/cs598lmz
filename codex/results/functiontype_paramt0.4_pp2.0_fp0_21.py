from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# ['x']

# __code__.co_varnames is a tuple of strings, giving the names of the local
# variables (starting with the argument names).

# Functions defined with the new lambda syntax (in Python 3) have no __code__
# attribute.

# Functions defined with the new lambda syntax (in Python 3) have no __code__
# attribute.

# The name of the function is available as __name__.

# The docstring of the function is available as __doc__.

# The function’s default arguments are available as __defaults__.

# The function’s closure is available as __closure__.

# The function’s globals as __globals__.

# The function’s module is available as __module__.

# The function’s dictionary is available as __dict__.

# The function’s annotations are available as __annotations__.


# Python 3.3 adds a __qualname__ attribute, which gives the fully
