fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in <lambda>
TypeError: 'generator' object is not callable
```

```
fn.__code__ = lambda: None
fn.__code__()
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not callable
```

## [`co_flags`](https://github.com/python/cpython/blob/f37c0f1e2b2d5f9e0e1a9e9baa7a8df6e4f7a1e6/Include/code.h#L136)

| Value | Description |
| --- | --- |
| `CO_OPTIMIZED` | `0x0001` |
| `CO_NEWLOCALS` | `
