import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return "Hello world"
print fun()
```

## Automatic support for tuples and lists

```
>>> import ctypes
>>> FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
>>> @FUNTYPE
... def fun(l): return l
>>> fun([1, 2, 3])
[1, 2, 3]
>>> fun((1, 2, 3))
(1, 2, 3)
```

## Automatic support for strings

```
>>> import ctypes
>>> FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p)
>>> @FUNTYPE
... def fun(s): return s
>>> s = fun(b"Hello world")
>>> s
'Hello world'
>>> type(s)
<class 'str'>
```

## Automatic support for buffers

```
>>> import ctypes
>>> FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
>>> @FUN
