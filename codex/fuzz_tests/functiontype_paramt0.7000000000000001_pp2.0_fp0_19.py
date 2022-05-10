from types import FunctionType
list(FunctionType(
    FunctionType.__code__,
    FunctionType.__globals__,
    name=FunctionType.__name__,
    argdefs=FunctionType.__defaults__,
    closure=FunctionType.__closure__
).__closure__)
```

```
>>> from types import FunctionType
>>> list(FunctionType(
...     FunctionType.__code__,
...     FunctionType.__globals__,
...     name=FunctionType.__name__,
...     argdefs=FunctionType.__defaults__,
...     closure=FunctionType.__closure__
... ).__closure__)
[<cell at 0x7f0d4e4c9a08: int object at 0x7f0d4d3f1580>, <cell at 0x7f0d4e4c9a48: int object at 0x7f0d4d3f1580>]
```

## 使用闭包

```python
def func(x):
    a = 1
    b = 2
    return
