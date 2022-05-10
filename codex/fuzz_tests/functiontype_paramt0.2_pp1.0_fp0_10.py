from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y']
list(FunctionType(lambda x, y: None, {}).__code__.co_varnames)

# ['x', 'y', 'z']
list(FunctionType(lambda x, y, z: None, {}).__code__.co_varnames)
</code>

