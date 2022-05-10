from types import FunctionType
list(FunctionType(lambda _: _, {}).__code__.co_varnames)

# ['_']
</code>

