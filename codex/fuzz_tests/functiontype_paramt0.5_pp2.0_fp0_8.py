from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())

# ['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__']
</code>
This is the same as the keys of the builtins module.

