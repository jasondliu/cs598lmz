from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f'))

# TypeError: 'function' object is not iterable
# list(function)

# TypeError: 'function' object is not iterable
# list(function())

# TypeError: 'function' object is not iterable
# list(function(1))

# TypeError: 'function' object is not iterable
# list(function(1, 2))

# TypeError: 'function' object is not iterable
# list(function(1, 2, 3))

# TypeError: 'function' object is not iterable
# list(function(1, 2, 3, 4))

# TypeError: 'function' object is not iterable
# list(function(1, 2, 3, 4, 5))

# TypeError: 'function' object is not iterable
# list(function(1, 2, 3, 4, 5, 6))

# TypeError: 'function' object is not iterable
# list(function(1, 2, 3, 4, 5, 6, 7))

# TypeError: '
