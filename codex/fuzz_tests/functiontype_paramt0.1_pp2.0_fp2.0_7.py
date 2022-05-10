from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z=None: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z=None, *args: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z=None, *args, **kwargs: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z=None, *args, **kwargs: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda
