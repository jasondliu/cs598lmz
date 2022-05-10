from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())
['__builtins__', '__doc__', '__file__', '__name__', '__package__']
</code>

