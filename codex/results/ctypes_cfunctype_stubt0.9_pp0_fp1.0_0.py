import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1.2
fun()
```

In this form, `fun` is not a Python object and does not have a 
corresponding Python type. The type is "function pointer", which 
corresponds to `void *` in C.

More specifically, it's not clear if the type is "function pointer" 
or "pointer to function (returning `py_object`)". Generally, in 
Python the former is indicated by function pointers and the latter 
by function objects. The functions defined by `FUNTYPE` are 
function pointers, not function objects.

`ctypes` also provides a declaration `ctypes.CFUNCTYPE(None)`. You 
can pass this type to `cast`, but it won't work because the assumed 
signature is `void()` (parameterless) instead of `void(*)()` 
(parameterless, but with unknown parameter list).

The closest you can get to the `fun` example is this:

```python
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
