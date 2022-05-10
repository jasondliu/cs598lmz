from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x']
</code>

