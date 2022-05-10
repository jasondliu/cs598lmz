from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo', (), (), None, None, None, None).__dict__.keys())

# ['__annotations__', '__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__name__', '__qualname__']

# __annotations__
# The dictionary of annotations for the function.

# __closure__
# The tuple of cell objects for the function.

# __code__
# The code object representing the compiled function body.

# __defaults__
# The tuple of default argument values for the function.

# __dict__
# The dictionary of the function’s attributes.

# __doc__
# The docstring for the function.

# __globals__
# The global namespace in which the function was defined.

# __name__
# The name of the function.

# __qualname__
# The qualified name of the function.
