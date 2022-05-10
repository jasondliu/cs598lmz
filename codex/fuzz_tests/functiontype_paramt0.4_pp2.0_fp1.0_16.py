from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# Output: ['x']
</code>

