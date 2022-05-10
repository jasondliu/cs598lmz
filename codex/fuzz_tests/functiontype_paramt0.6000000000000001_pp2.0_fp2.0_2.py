from types import FunctionType
list(FunctionType(lambda: None).__dict__.keys())

# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__module__', '__name__', '__qualname__']
</code>

