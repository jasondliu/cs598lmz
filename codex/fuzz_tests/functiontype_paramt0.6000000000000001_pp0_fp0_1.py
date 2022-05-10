from types import FunctionType
list(FunctionType(lambda x: x+1, {}, "f", (object,), 0).__code__.co_varnames)

# Output:
['x']
</code>

