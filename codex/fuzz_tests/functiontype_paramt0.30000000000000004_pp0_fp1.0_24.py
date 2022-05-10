from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__annotations__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# >>>
# >>> list(FunctionType(lambda: None, {}).__code__.co_varnames)
# ['__annotations__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
# >>> list(FunctionType(lambda: None, {}).__code__.co_varnames)
# ['__annotations__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
# >>> list(FunctionType(lambda: None, {}).__code__.co_varnames)
