import ctypes
ctypes.cast(1, ctypes.py_object)

#1 <type 'int'>
#>>> ctypes.cast(1, ctypes.py_object).value
#1
#>>> type(ctypes.cast(1, ctypes.py_object).value)
#<type 'int'>
#>>> ctypes.cast("s", ctypes.py_object).value
#'s'
#>>> type(ctypes.cast("s", ctypes.py_object).value)
#<type 'str'>
#>>> ctypes.cast(1.1, ctypes.py_object).value
#1.1
#>>> type(ctypes.cast(1.1, ctypes.py_object).value)
#<type 'float'>
#>>> ctypes.cast("s", ctypes.py_object)
#c_char_p(u's')
#>>> ctypes.cast("s", ctypes.py_object).value
#'s'
#>>> ctypes.cast("s", ctypes.py_object).value
#'s'
#>>> ctypes.cast("
