from types import FunctionType
list(FunctionType(f.__code__, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtins__', '__file__', '__cached__', '__builtins__']
</code>

