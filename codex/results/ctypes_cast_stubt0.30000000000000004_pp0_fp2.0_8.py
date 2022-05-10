import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# or

obj.__dict__

# or

type(obj).__dict__['attr'].__get__(obj)
</code>

