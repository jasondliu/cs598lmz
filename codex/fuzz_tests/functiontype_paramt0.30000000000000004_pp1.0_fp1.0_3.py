from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(2))
# [<function foo at 0x7f9f9c7c9488>, <function foo at 0x7f9f9c7c9400>]
```

The `globals()` argument is optional.

#### `FunctionType.__code__`

```python
from types import FunctionType
FunctionType(lambda: None, globals(), 'foo').__code__
# <code object foo at 0x7f9f9c7c9c20, file "<stdin>", line 1>
```

#### `FunctionType.__closure__`

```python
from types import FunctionType
FunctionType(lambda: None, globals(), 'foo').__closure__
# None
```

#### `FunctionType.__dict__`

```python
from types import FunctionType
FunctionType(lambda: None, globals(), 'foo').__dict__
# {}
```

#### `FunctionType.__doc__`

```python
from types import FunctionType

