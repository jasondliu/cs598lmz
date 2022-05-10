from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__qualname__', '__module__', '__doc__', '__annotations__', '__kwdefaults__', '__defaults__', '__code__', '__globals__', '__dict__', '__closure__', '__name__', '__dict__', '__weakref__', '__text_signature__', '__module__', '__defaults__', '__kwdefaults__', '__annotations__', '__closure__', '__code__', '__globals__', '__dict__', '__name__', '__qualname__', '__defaults__', '__kwdefaults__', '__annotations__', '__closure__', '__code__', '__globals__', '__dict__', '__name__', '__qualname__', '__defaults__', '__kwdefaults__', '__annotations__', '__closure__', '__code__', '__globals__', '__dict__', '__name__',
