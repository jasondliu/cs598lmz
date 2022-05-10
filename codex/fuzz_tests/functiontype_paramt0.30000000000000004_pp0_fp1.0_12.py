from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__lambda__']
</code>

