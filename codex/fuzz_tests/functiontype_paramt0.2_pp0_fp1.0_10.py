from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

# Output:
# [<function __main__.<lambda>>, <function __main__.<lambda>>, <function __main__.<lambda>>]
```

### `inspect.getmembers`

```python
import inspect

def f():
    pass

inspect.getmembers(f, predicate=inspect.isfunction)

# Output:
# [('__call__', <method-wrapper '__call__' of function object at 0x7f6c8e8f4ea0>)]
```

### `inspect.getmodule`

```python
import inspect

def f():
    pass

inspect.getmodule(f)

# Output:
# <module '__main__' from '/home/user/main.py'>
```

### `inspect.getmro`

```python
import inspect

class A:

