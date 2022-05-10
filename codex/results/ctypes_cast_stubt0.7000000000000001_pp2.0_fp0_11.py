import ctypes
ctypes.cast(0, ctypes.py_object)
```

```
>>> ctypes.cast(0, ctypes.py_object)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```

### [ctypes.cast()](https://docs.python.org/3/library/ctypes.html#ctypes.cast)
```
ctypes.cast(obj, type)
```

> Cast an object to a type.

### [ctypes.POINTER()](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER)
```
ctypes.POINTER(type)
```

> Return a new object which represents a pointer to the given type.

```
>>> ctypes.POINTER(ctypes.py_object)
<class 'ctypes.POINTER(py_object)'>
```

### [ctypes.addresso
