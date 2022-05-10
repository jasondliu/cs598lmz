from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

# ['x', 'y']

list(FunctionType(lambda x, y: 0, {}).__code__.co_varnames)

# ['x', 'y']

list(FunctionType(lambda x, y=1: 0, {}).__code__.co_varnames)

# ['x', 'y']

list(FunctionType(lambda x, *, y: 0, {}).__code__.co_varnames)

# ['x', 'y']

list(FunctionType(lambda x, *args, y: 0, {}).__code__.co_varnames)

# ['x', 'args', 'y']

list(FunctionType(lambda x, *args, y=1: 0, {}).__code__.co_varnames)

# ['x', 'args', 'y']

list(FunctionType(lambda x, *, y=1: 0, {}).__code__.co_varnames)

# ['x', '
