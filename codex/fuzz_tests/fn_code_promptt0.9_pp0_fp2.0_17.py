fn = lambda: None
# Test fn.__code__ and fn.__defaults__

setattr(fn, '__code__', 1)
setattr(fn, '__defaults__', 1)

with self_check():
    (setattr(fn, '__code__', 1) and
     setattr(fn, '__defaults__', 1))
```

```diff
- assert setattr(fn, '__code__', 1)
- assert setattr(fn, '__defaults__', 1)
+ setattr(fn, '__code__', 1)
+ setattr(fn, '__defaults__', 1)
```

```py
# Test fn.__slots__

setattr(fn, '__slots__', 1)

with self_check():
    setattr(fn, '__slots__', 1)
```

```diff
- assert setattr(fn, '__slots__', 1)
+ setattr(fn, '__slots__', 1)
```

```py
# Test fn.__closure__

setattr(
