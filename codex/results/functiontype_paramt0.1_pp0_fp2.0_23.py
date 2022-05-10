from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y']
list(FunctionType(lambda x, y: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z: None, {}).__code__.co_varnames)

# ['x', 'y', 'z', 'w']
list(FunctionType(lambda x, y, z, w: None, {}).__code__.co_varnames)

# ['x', 'y', 'z', 'w', 'a']
list(FunctionType(lambda x, y, z, w, a: None, {}).__code__.co_varnames)

# ['x', 'y', 'z', 'w', 'a', 'b']
list(FunctionType(lambda x, y, z, w, a, b: None, {}).__code__.co_varnames)

# ['x', 'y', 'z', 'w', 'a', '
