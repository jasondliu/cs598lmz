import ctypes
ctypes.cast(0, ctypes.py_object)

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = None

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = 0

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = 1

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = 1.0

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = 'a'

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = 'abc'

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = b'a'

# This will raise an exception
ctypes.cast(0, ctypes.py_object).value = b'abc'


