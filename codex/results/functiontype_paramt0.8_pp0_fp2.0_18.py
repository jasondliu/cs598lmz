from types import FunctionType
list(FunctionType(lambda x: x * 2, {}, None, None, None).__globals__.keys())

# ['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtin__', '__file__', '__cached__', '__all__']
```

可以看到这些是不可达的全局变量，这些变量最终都是在 `__builtins__.__dict__` 中。我们可以这样做来恢复它们：

```python
import builtins

import __builtin__

def __import__(name, globals=None, locals=None, fromlist=(), level=0):
    return __builtin__.__import__(name, globals, locals, fromlist, level)

builtins.__import
