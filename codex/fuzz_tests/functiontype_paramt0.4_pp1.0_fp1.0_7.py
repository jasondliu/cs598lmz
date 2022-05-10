from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in [lambda a, b: a + b, lambda a, b: a - b])

# [<function <lambda> at 0x7f8b6d7b9488>, <function <lambda> at 0x7f8b6d7b9510>]
```

## `inspect.getfullargspec`

```python
# inspect.getfullargspec(func)

# Get the names and default values of a Python function's arguments.
# A tuple of four things is returned: (args, varargs, varkw, defaults).
# 'args' is a list of the argument names (it may contain nested lists).
# 'varargs' and 'varkw' are the names of the * and ** arguments or None.
# 'defaults' is an n-tuple of the default values of the last n arguments.
```

```python
import inspect

