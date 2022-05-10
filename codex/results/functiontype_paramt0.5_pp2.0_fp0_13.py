from types import FunctionType
list(FunctionType(lambda x: x ** 2, globals(), 'square')(i) for i in range(5))
 
# >>> [0, 1, 4, 9, 16]

# >>> [function(i) for i in range(5)]
# [0, 1, 4, 9, 16]

# >>> list(map(function, range(5)))
# [0, 1, 4, 9, 16]

# >>> import functools
# >>> list(map(functools.partial(function, exponent=2), range(5)))
# [0, 1, 4, 9, 16]

# >>> list(map(lambda i: function(i, exponent=2), range(5)))
# [0, 1, 4, 9, 16]

# >>> [function(i, exponent=2) for i in range(5)]
# [0, 1, 4, 9, 16]

# >>> list(function(i, exponent=2) for i in range(5))
# [0, 1, 4, 9, 16]

# >>> import operator
# >>> list(map(
