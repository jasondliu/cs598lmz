fn = lambda: None
# Test fn.__code__
>>> fn.__code__.co_argcount
Traceback (most recent call last):
    ...
AttributeError: 'NoneType' object has no attribute '__code__'
# Test inspect module
>>> _ = type(inspect.__code__)
<class 'code'>
```

But `inspect.getclosurevars(fn)` still works. This is because `fn` actually has a `func_closure` of
`(a, b)`, so `inspect.getclosurevars(fn)` can find these names.
However, `inspect.signature(fn)` raises error, because `fn.__code__` can't be found.

```
# Test `fn` has a closure
>>> fn.__closure__
(<cell at 0x7fba594a77c8: int object at 0x55ff64bab8d0>, <cell at 0x7fba594a7898: str object at 0x55ff64e97300>)
# Test getclosurevars(fn)
>>> inspect.getclosurevars(fn)

