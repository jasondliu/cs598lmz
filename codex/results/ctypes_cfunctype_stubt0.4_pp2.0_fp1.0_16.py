import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

assert fun() == "hello"
```

### `ctypes.c_void_p`

`ctypes.c_void_p` is the type of a pointer to a C `void`.

```python
from ctypes import c_void_p

def f(x):
    return x

assert f(c_void_p(0)) == c_void_p(0)
```

### `ctypes.c_char_p`

`ctypes.c_char_p` is the type of a pointer to a C `char`.

```python
from ctypes import c_char_p

def f(x):
    return x

assert f(c_char_p(b"hello")) == c_char_p(b"hello")
```

### `ctypes.c_wchar_p`

`ctypes.c_wchar_p` is the type of a pointer to a C `wchar_t`.

```python
from ctypes import c_wchar_p
