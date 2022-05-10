from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda x: x, lambda x, y: x + y))
# [<function <lambda> at 0x7f0d8a8e9b90>, <function <lambda> at 0x7f0d8a8e9c80>]
```

### `get_function_code`

```python
from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda x: x, lambda x, y: x + y))
# [<function <lambda> at 0x7f0d8a8e9b90>, <function <lambda> at 0x7f0d8a8e9c80>]
```

### `get_function_closure`
