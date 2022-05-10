fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError()
```

```python
# Updating __code__ object with a correct object is ok
fn = lambda: None
fn.__code__ = fn.__code__
```

```python
# Updating __code__ object with a non-code object is ok
fn = lambda: None
del fn.__code__
fn.__code__ = None

try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError()
```

```python
# Updating __code__ object with a non-code object is ok
fn = lambda: None
fn.__code__ = None

try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError()
```

### __doc__, __repr__
Make sure `__doc__` and `__repr__` are not overriden if doing so would cause
deprecation warnings.
