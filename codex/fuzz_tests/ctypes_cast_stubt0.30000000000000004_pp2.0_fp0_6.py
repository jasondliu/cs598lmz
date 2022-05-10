import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# or

obj.__dict__

# or

type(obj).__dict__['x'].__get__(obj, type(obj))
</code>

