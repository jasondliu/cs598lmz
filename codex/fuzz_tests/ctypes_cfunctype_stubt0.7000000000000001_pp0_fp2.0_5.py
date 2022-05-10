import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    p = P.call_me()
    return p

lib.fun = fun
```

```shell
$ python test.py
```
