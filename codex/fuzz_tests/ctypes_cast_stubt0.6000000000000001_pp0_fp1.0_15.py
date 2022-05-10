import ctypes
ctypes.cast(0, ctypes.py_object).value

# Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
# [GCC 4.6.3] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ctypes
# >>> ctypes.cast(0, ctypes.py_object).value
# 0
# >>> ctypes.cast(0, ctypes.py_object).value = 1
# >>> ctypes.cast(0, ctypes.py_object).value
# 1
# >>> ctypes.cast(0, ctypes.py_object).value = [1,2,3]
# >>> ctypes.cast(0, ctypes.py_object).value
# [1, 2, 3]
# >>> ctypes.cast(0, ctypes.py_object).value = 'Hello'
# >>> ctypes.cast(0, ctypes.py_object).value
# 'Hello'
# >>> ctypes.cast(0, ctypes.py_object).value =
