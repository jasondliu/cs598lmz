from types import FunctionType
list(FunctionType(lambda x: x, {}).__dict__)

# Output:
# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
</code>

