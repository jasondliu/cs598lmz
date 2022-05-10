import ctypes
ctypes.cast(0, ctypes.py_object)

# prints "c_void_p(None)"
```

```python
# python2
ctypes.cast(0, ctypes.py_object)

# prints "<cparam 'P' c_void_p(0)>"
```

```python
ctypes.cast(0, ctypes.c_void_p).value

# prints 0
```

```python
# python2
ctypes.cast(0, ctypes.c_void_p).value

# prints 0
```

```python
ctypes.cast(0, ctypes.c_void_p)

# prints "c_void_p(0)"
```

```python
# python2
ctypes.cast(0, ctypes.c_void_p)

# prints "<cparam 'P' c_void_p(0)>"
```

```python
ctypes.cast(0, ctypes.py_object).value

# prints None
```

``
