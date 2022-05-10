fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', type('code', (object,), {'co_varnames': ('x', 'y')}))
print(fn.__code__.co_varnames)
# ('x', 'y')
```

```python
# fn.__defaults__
fn = lambda x, y=33: None
# Test fn.__defaults__
setattr(fn, '__defaults__', (11,))
print(fn.__defaults__)
# (11,)
```

```python
# fn.__kwdefaults__
fn = lambda x, y=33: None
# Test fn.__kwdefaults__
setattr(fn, '__kwdefaults__', {'z': 44})
print(fn.__kwdefaults__)
# {'z': 44}
```

```python
# fn.__annotations__
fn = lambda x, y=33: None
# Test fn.__annotations__
setattr(fn, '__annotations__',
