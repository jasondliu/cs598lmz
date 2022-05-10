from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())

# [..., '__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__file__', '__cached__', '__builtins__', '__file__', '__cached__', '__loader__', '__name__', '__package__', '__spec__', '__annotations__', '__doc__', '__builtins__', '__file__', '__cached__', '__loader__', '__name__', '__package__', '__spec__', '__annotations__', '__doc__', '__builtins__', '__file__', '__cached__', '__loader__', '__name__', '__package__', '__spec__', '__annotations__', '__doc__', '__builtins__', '__file__', '__cached__', '__loader__', '__name__', '__package__', '__spec__', '__annotations__',
