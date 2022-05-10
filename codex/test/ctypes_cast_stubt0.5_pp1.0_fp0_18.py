import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# Or if you want to use the __dict__ of the type, you can use the following:
import ctypes
ctypes.cast(id(int), ctypes.py_object).value.__dict__
