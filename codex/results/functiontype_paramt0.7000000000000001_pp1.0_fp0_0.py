from types import FunctionType
list(FunctionType(f.__code__, d).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'f', 'a']
</code>

