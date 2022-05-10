import ctypes
ctypes.cast(obj, ctypes.py_object).value

# 2.6
obj.__class__.__base__.__base__.__base__.value

# 2.7
obj.__class__.__bases__[0].__bases__[0].__bases__[0].value
</code>

