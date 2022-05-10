from types import FunctionType
list(FunctionType(lambda x: x, globals()).__globals__.keys())

# ['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__',
#  '__annotations__', '__builtin_module_names__', '__file__', '__cached__',
#  '__initializing__', '__main__', '__spec__', '__loader__', '__name__', '__package__',
#  '__path__', '__doc__', '__all__', '__author__', '__copyright__', '__license__',
#  '__version__', '__email__', '__status__', '__date__', '__credits__']
```

```bash

```

```
```
