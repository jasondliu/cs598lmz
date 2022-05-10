from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda").__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__']
```

```python
import types
types.FunctionType(lambda x: x, globals(), "lambda").__globals__.keys()

# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__', '__name__', '__doc__', '__package__', '
