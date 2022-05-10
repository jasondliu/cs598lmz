from types import FunctionType
list(FunctionType(lambda: None, globals(), '', (), None).__code__.co_varnames)

# ['f']
</code>

