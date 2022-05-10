from types import FunctionType
list(FunctionType(lambda: 0, {}, '', (), None, None).__code__.co_varnames)

# ['a', 'b', 'c', 'd', 'e']
</code>

