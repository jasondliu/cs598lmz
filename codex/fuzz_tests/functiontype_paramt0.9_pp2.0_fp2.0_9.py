from types import FunctionType
list(FunctionType(f.__code__)(1, 2)) == [1, 2]
```

```python
f = lambda x, y: (x, y)
f.__code__.co_varnames
tuple(f.__defaults__)

```

```
>>> pc = to_bytecode(f)
>>> f.__code__.co_code == pc.__code__.co_code
True

In [20]: dis.dis(f)                                                                                                                                                                                                                                 
  2           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BUILD_TUPLE              2
              6 RETURN_VALUE        
```



### Check for "Ready for prime time"

```python
import inspect
... 
def f(x, y):
    return x + y
... 
inspect.getfullargspec(f)
# FullArgSpec(args=['x', 'y'], varargs=None, varkw=None,
