import ctypes
ctypes.cast(0, ctypes.py_object)

# prints <class 'int'>
# ctypes.cast(0, ctypes.py_object) is a Python Object
print(type(ctypes.cast(0, ctypes.py_object)))

# prints <class 'int'>
# ctypes.cast(0, ctypes.py_object) is a Python Object
# and its type is <class 'int'>
print(type(ctypes.cast(0, ctypes.py_object)).__name__)

# prints 0
# ctypes.cast(0, ctypes.py_object) is a Python Object
# and its value is 0
print(ctypes.cast(0, ctypes.py_object))

# prints <class 'str'>
# ctypes.cast('Hello', ctypes.py_object) is a Python Object
# and its type is <class 'str'>
print(type(ctypes.cast('Hello', ctypes.py_object)))

# prints 'Hello'
# ctypes.cast('Hello', ctypes.py_object) is a Python Object
