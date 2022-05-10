fn = lambda: None
# Test fn.__code__.co_names
setattr(fn, '__code__', fn.__code__.replace(names=['a', 'b']))
print(fn.__code__.co_names)
# ('a', 'b')

# Test fn.__closure__
fn.__closure__ = (lambda: None, lambda: None)
print(fn.__closure__)
# (None, None)
```

## Todo

- [x] Structured properties
- [ ] Add support for dict and namedtuple
- [ ] Argument unpacking with *args and **kwargs
- [ ] Hashable and non-hashable types
- [ ] Pickle support
