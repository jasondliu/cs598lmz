from types import FunctionType
list(FunctionType(lambda: 1, {}).__code__.co_freevars)

# >>> list(FunctionType(lambda: 1, {}).__code__.co_freevars)
# []

# >>> list(FunctionType(lambda x: 1, {}).__code__.co_freevars)
# []

# >>> list(FunctionType(lambda: x, {'x': 1}).__code__.co_freevars)
# ['x']

# >>> list(FunctionType(lambda x: x, {'x': 1}).__code__.co_freevars)
# []

# >>> list(FunctionType(lambda x: y, {'x': 1}).__code__.co_freevars)
# ['y']

# >>> list(FunctionType(lambda x: y, {'x': 1, 'y': 2}).__code__.co_freevars)
# ['y']

# >>> list(FunctionType(lambda x: y, {'x': 1, 'y': 2, 'z': 3}).__code__.co
