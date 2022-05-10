from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())

# Output:
['__name__',
 '__doc__',
 '__package__',
 '__loader__',
 '__spec__',
 '__annotations__',
 '__builtins__',
 '__file__',
 '__cached__',
 '__builtin_module_names__']
</code>

