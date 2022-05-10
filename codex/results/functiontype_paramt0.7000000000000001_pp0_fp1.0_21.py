from types import FunctionType
list(FunctionType(f.__code__, {}).__globals__.keys())

# py2.6
In [6]: f.func_code.co_names
Out[6]: ('type',)

In [7]: map(f.func_globals.__getitem__, f.func_code.co_names)
Out[7]: (<type 'type'>,)

# py3.3
In [7]: f.__code__.co_names
Out[7]: ('type',)

In [7]: map(f.__globals__.__getitem__, f.__code__.co_names)
Out[7]: (<class 'type'>,)
```


## 获取函数的属性

- inspect.getfullargspec
- inspect.getargspec
- inspect.getargvalues

```python
import inspect

class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b

print(inspect.getarg
