fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
```

```python
import ctypes
fn = lambda: None
gi = (i for i in ())
libc = ctypes.cdll.LoadLibrary('libc.so.6')
fn.__code__ = gi.gi_code
libc.setcontext()
```

```python
import ctypes
fn = lambda: None
gi = (i for i in ())
libc = ctypes.cdll.LoadLibrary('libc.so.6')
fn.__code__ = gi.gi_code
libc.sigsetmask()
```

```python
import ctypes
fn = lambda: None
gi = (i for i in ())
libc = ctypes.cdll.LoadLibrary('libc.so.6')
fn.__code__ = gi.gi_code
libc.sigprocmask()
```

## linux

```python
import ctypes
fn = lambda: None
gi = (i for i in ())
libc = ctypes.cdll
