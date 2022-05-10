from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# Output:
# [<class 'function'>, <class 'method'>, <class 'builtin_function_or_method'>, <class 'builtin_function_or_method'>, <class 'method_descriptor'>, <class 'wrapper_descriptor'>, <class 'method-wrapper'>]

# The first three are the most important.
# The first is the function object itself.
# The second is the function object when it is bound to an object.
# The third is the function object when it is a built-in function.

# The other types are internal to Python.
# They are used to implement descriptors, methods, and other internal functionality.

# The function object itself is the most important.
# It is the object that is returned by the def statement.
# It is also the object that is assigned to a variable when you use the lambda statement.

# The function object has the following attributes:

# __doc__: The docstring of the function.
# __name__: The name of the function.
# __qualname
