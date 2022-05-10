import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError
ctypes.cast(0, ctypes.py_object)

# AttributeError
ctypes.cast(0, ctypes.py_object).value = 0

# TypeError
ctypes.cast(0, ctypes.py_object).value = None

# TypeError
ctypes.cast(0, ctypes.py_object).value = 'abc'

# TypeError
ctypes.cast(0, ctypes.py_object).value = b'abc'

# TypeError
ctypes.cast(0, ctypes.py_object).value = []

# TypeError
ctypes.cast(0, ctypes.py_object).value = ()

# TypeError
ctypes.cast(0, ctypes.py_object).value = {}

# TypeError
ctypes.cast(0, ctypes.py_object).value = set()

# TypeError
ctypes.cast(0, ctypes.py_object).value = frozenset()

# TypeError
ctypes
