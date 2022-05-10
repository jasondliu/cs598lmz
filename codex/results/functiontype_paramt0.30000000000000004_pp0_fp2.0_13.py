from types import FunctionType
list(FunctionType(lambda x: x, globals()).__code__.co_varnames)

# ['x']
</code>

