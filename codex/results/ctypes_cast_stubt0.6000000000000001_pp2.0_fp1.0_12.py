import ctypes
ctypes.cast(1, ctypes.py_object)

# TypeError: an integer is required (got type str)
s = 'hello world'
ctypes.cast(s, ctypes.c_char_p)
```

### `ctypes.py_object`

`ctypes.py_object`: ctypes type representing the Python `object` type.

```python
import ctypes
ctypes.py_object

# <class 'ctypes.py_object'>
ctypes.py_object

# <class 'ctypes.c_int'>
ctypes.c_int
```

### `ctypes.c_int`

`ctypes.c_int`: ctypes type representing the C `int` type.

```python
import ctypes
ctypes.c_int

# <class 'ctypes.c_int'>
ctypes.c_int

# <class 'ctypes.py_object'>
ctypes.py_object
```

### `ctypes.create_string_buffer`

`ctypes.create
