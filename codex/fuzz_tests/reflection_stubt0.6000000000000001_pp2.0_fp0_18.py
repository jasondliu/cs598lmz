fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
fn.__qualname__ = 'test'
print(fn)
```

# python3.7
```
class test:
    def __init__(self):
        pass

test.__code__ = (i for i in ()).gi_code
test.__name__ = 'test'
test.__qualname__ = 'test'
print(test)
```

# python3.8
```
class test:
    def __init__(self):
        pass

test.__code__ = (i for i in ()).gi_code
test.__name__ = 'test'
test.__qualname__ = 'test'
print(test)
```

# python3.9
```
class test:
    def __init__(self):
        pass

test.__code__ = (i for i in ()).gi_code
test.__name__ = 'test'
test.__qualname__ = 'test'
print(test)
```
