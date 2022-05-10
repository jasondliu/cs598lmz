import ctypes
ctypes.cast(obj, ctypes.py_object).value

# Or alternatively:

ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
ctypes.pythonapi.PyCObject_AsVoidPtr(obj)

Example:

obj = 'this is a string'

ptr = ctypes.cast(id(obj), ctypes.c_void_p).value
print(ptr)
# Outputs: 2958120982992

# WILL FAIL
print(ctypes.cast(2826430365376, ctypes.c_char_p).value)
# Segmentation fault: 11

print(ctypes.cast(2958120982992, ctypes.c_char_p).value)
# Outputs: b'this is a string'

print(ctypes.cast(2958120982992, ctypes.py_object).value)
# Outputs: 'this
