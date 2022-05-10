fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

```
Traceback (most recent call last):
  File "./crash.py", line 5, in <module>
    fn()
TypeError: 'generator' object is not callable
```

### Bug 2

```python
import sys

class Foo:
    def __init__(self):
        self.__class__ = sys.modules[__name__]

f = Foo()
```

```
Traceback (most recent call last):
  File "./crash.py", line 10, in <module>
    f = Foo()
  File "./crash.py", line 5, in __init__
    self.__class__ = sys.modules[__name__]
  File "./crash.py", line 5, in __init__
    self.__class__ = sys.modules[__name__]
  File "./crash.py", line 5, in __init__
    self.__class__ = sys.modules[__name__]
  [Previous line repeated 996
