import ctypes
ctypes.cast(obj, ctypes.py_object).value

# the same thing, but in the interactive interpreter
# it looks like a tuple, but it is not:
>>> obj.contents
(1, 2, 3)
>>> type(obj.contents)
<class '__main__.c_int_Array_3'>

# convert it to a real tuple
>>> tuple(obj.contents)
(1, 2, 3)

# assign a new value to an element of the array
>>> obj.contents[0] = 42

# the array changed, of course:
>>> obj.contents
(42, 2, 3)

# the original Python object also changed:
>>> obj.value
(42, 2, 3)

# assign a new value to the entire array
>>> obj.contents = (4, 5, 6)
>>> obj.contents
(4, 5, 6)
>>> obj.value
(4, 5, 6)

# now we have a different array:
>>> obj.contents is array
False
```

## How to use the `_
