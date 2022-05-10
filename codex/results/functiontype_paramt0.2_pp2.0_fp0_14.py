from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# ['a', 'b', 'c']
</code>

