from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c']
</code>

