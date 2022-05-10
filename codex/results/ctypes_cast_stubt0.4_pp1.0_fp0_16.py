import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# For example:

obj = [1, 2, 3]
ctypes.cast(id(obj), ctypes.py_object).value
# [1, 2, 3]

obj = 'abc'
ctypes.cast(id(obj), ctypes.py_object).value
# 'abc'

obj = {'a': 1, 'b': 2}
ctypes.cast(id(obj), ctypes.py_object).value
# {'a': 1, 'b': 2}

obj = (1, 2, 3)
ctypes.cast(id(obj), ctypes.py_object).value
# (1, 2, 3)

obj = 1
ctypes.cast(id(obj), ctypes.py_object).value
# 1

obj = 1.0
ctypes.cast(id(obj), ctypes.py_object).value
# 1.0

obj = True
ctypes.cast(id(obj), ctypes.py_object).value
# True

obj
