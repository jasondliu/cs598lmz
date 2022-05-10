from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

# ['__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__name__', '__qualname__']
</code>

