fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # this should raise a TypeError
assert False, "didn't raise TypeError"
```

```
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    assert False, "didn't raise TypeError"
AssertionError: didn't raise TypeError
```

`fn.__code__ = gi` raises a TypeError.

## Fixed in 3.9

```python
def f():
    pass

def g():
    pass

def h():
    pass

f.__code__ = g.__code__
h.__code__ = g.__code__

assert f.__code__ is g.__code__
assert h.__code__ is g.__code__
```

## Fixed in 3.10

```python
import inspect

class Foo:
    def __call__(self):
        return 1

f = Foo()
f.__code__ = 1  # this should raise a TypeError
assert False, "didn't raise TypeError"

