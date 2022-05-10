import ctypes
ctypes.cast(0, ctypes.py_object)

# prints <class 'ctypes.py_object'>
print(type(ctypes.cast(0, ctypes.py_object)))

# prints <class 'int'>
print(type(ctypes.cast(0, ctypes.py_object).value))

# prints <class 'bool'>
print(type(bool(ctypes.cast(0, ctypes.py_object))))

# prints <class 'bool'>
print(type(bool(ctypes.cast(1, ctypes.py_object))))

# prints <class 'bool'>
print(type(bool(ctypes.cast(0.0, ctypes.py_object))))

# prints <class 'bool'>
print(type(bool(ctypes.cast(0.1, ctypes.py_object))))

# prints <class 'bool'>
print(type(bool(ctypes.cast(None, ctypes.py_object))))

# prints <class 'bool'>
print(type(bool(ctypes.cast('', ctypes.py_object))))
