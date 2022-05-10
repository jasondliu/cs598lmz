from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# ['x', 'y']
</code>

