import ctypes
ctypes.cast(id(obj),ctypes.py_object).value

#Using __reduce__
import pickle
pickle.dumps(obj)
```

With this knowledge, and the fact that `__reduce__` is accessible via `dir(obj)`, and `_repr_html_` is accessible via `dir(obj)`, we can abuse the second by creating an object that returns our crafted `__reduce__` payload.

## Exploit

```python
import pickle

class Exploit(object):
    def _repr_html_(self):
        return 'a:1:{i:0;O:12:"SSTIMER_SLEEP":2:{s:4:"name";s:4:"test";s:4:"stop";R:14;}}'

pickle.dumps(Exploit())
```

## Docker Build

```bash
docker build . -t pickle_exploit:latest
docker run -it pickle_exploit
```
