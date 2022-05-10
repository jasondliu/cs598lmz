from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, 'f', f.__defaults__, f.__closure__))

# but this works:
f = lambda: x
list(f.__closure__)
'x' in globals()

# this works too:
f = lambda: x
list(f.__closure__)
'x' in globals()

# But this fails:
def f():
    return x
list(f.__closure__)
'x' in globals()

# But this succeeds:
def f():
    return x
list(f.__closure__)
'x' in globals()
```

```
#!/usr/bin/env python

# This fails:
f = lambda: x
list(f.__closure__)

# This succeeds:
f = lambda: x
list(f.__closure__)
```

```
#!/usr/bin/env python

# This fails:
f = lambda: x
list(f.__closure__)
'x' in glob
