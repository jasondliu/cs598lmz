from types import FunctionType
list(FunctionType(lambda: 0, {}).__globals__.keys())

## [out]: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names']
</code>

