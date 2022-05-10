from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10)), lambda x=5: (yield from range(x))))
# [<function <lambda> at 0x7f8d8f8a9488>, <function <lambda> at 0x7f8d8f8a9400>]
```

### `inspect.isgeneratorfunction(obj)`

Return `True` if the object is a user-defined generator function.

```python
import inspect
def f():
    yield from range(10)
inspect.isgeneratorfunction(f)
# True
```

### `inspect.isgenerator(obj)`

Return `True` if the object is a generator.

```python
import inspect
def f():
    yield from range(10)
inspect.isgenerator(f())
# True
```

### `inspect.
