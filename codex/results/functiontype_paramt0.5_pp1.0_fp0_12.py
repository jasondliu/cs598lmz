from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'foo'))

# TypeError: 'function' object is not iterable
# list(lambda x: x+1)

# TypeError: 'function' object is not iterable
# list(lambda x: x+1())

# TypeError: 'function' object is not iterable
# list(lambda x: x+1(1))

# TypeError: 'function' object is not iterable
# list(lambda x: x+1(1, 2))

# TypeError: 'function' object is not iterable
# list(lambda x: x+1(1, 2, 3))

# TypeError: 'function' object is not iterable
# list(lambda x: x+1(1, 2, 3, 4))

# TypeError: 'function' object is not iterable
# list(lambda x: x+1(1, 2, 3, 4, 5))

# TypeError: 'function' object is not iterable
# list(lambda x: x+1(1, 2, 3, 4, 5, 6
