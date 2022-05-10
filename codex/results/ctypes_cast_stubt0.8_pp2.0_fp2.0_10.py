import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# For example:
ctypes.cast(id(1), ctypes.py_object).value

# ==> 1
```

### An example:

```python
obj = 1

# change obj to 2
ctypes.cast(id(obj), ctypes.py_object).value = 2

# obj is still 1
print(obj)
```

### Reference counted objects

Python objects are typically reference counted. If reference count gets to `0`, the object is destroyed and memory is freed.

```python
>>> import sys

>>> x = 1
>>> sys.getrefcount(x)

# ==> 2
```

```python
>>> x = 1
>>> x in locals()

# ==> True

>>> x = [1,2,3]
>>> x in locals()

# ==> True

>>> x = None # reference count == 0
>>> x in locals()

# ==> False
```

### Interned objects

When it comes to strings, Python
