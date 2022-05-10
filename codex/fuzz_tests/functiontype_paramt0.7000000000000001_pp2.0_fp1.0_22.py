from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo").__globals__.keys())

# ['__package__', '__spec__', '__loader__', '__name__', '__doc__', '__file__', '__cached__', '__builtins__', '__loader__', '__doc__', '__spec__', '__name__', '__file__', '__cached__', '__builtins__', 'f', 'foo', 'sys', 'FunctionType', 'bar', 'baz', 'quux']

# dir(f)
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__
