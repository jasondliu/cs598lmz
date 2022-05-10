from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), 'square')(i) for i in range(5))

# [0, 1, 4, 9, 16]

# The first argument is the function body, the second is the global namespace,
# and the third is the function name.

# The function body is a single expression, not a series of statements.
# This is the same as the lambda syntax in Python.

# The function body can be passed in as a string.
list(FunctionType(compile('x', '', 'eval'), globals(), 'square')(i) for i in range(5))

# [0, 1, 4, 9, 16]

# The function body can also be passed in as a code object.
list(FunctionType(compile('x**2', '', 'eval'), globals(), 'square')(i) for i in range(5))

# [0, 1, 4, 9, 16]

# The function body can be passed in as a code object.
list(FunctionType(compile('x**2', '', 'eval'), globals(),
