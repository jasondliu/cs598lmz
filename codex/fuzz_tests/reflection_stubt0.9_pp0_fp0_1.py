fn = lambda: None
gi = (i for i in ())
fn.__code__ = [0, 1]
gi.gi_frame.f_locals = {'__class__': fn}
fn.__code__ = None
str(gi)
``` -->
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 1, in <module>
TypeError: can't set attribute
```

There is an analogous gi-frame-code-cant-be-deleted-via-properties.py
exploitation vector.

## Exploit

The exploit also works on Python versions that are compiled with --with-pydebug.
For example, releases after Python 3.3.3 are compiled with --with-pydebug.
The reason it works is because gc.get_count is not compiled with
Py_TRACE_REFS. No Py_TRACE_REFS means that decrementing the refcount of
actually decrements the refcount.
