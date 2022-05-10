import ctypes
ctypes.cast(2, ctypes.py_object)
 
# _Py_NoneStruct is an alias for None
ctypes.cast(None, ctypes.py_object)

# ints are cast to long
ctypes.cast(2, ctypes.py_object)

# so are floats
ctypes.cast(2.0, ctypes.py_object)

# None is cast to Py_None
ctypes.cast(None, ctypes.py_object)

# str is cast to PyStringObject
ctypes.cast("abc", ctypes.py_object).ob_refcnt
ctypes.cast("abc", ctypes.py_object).ob_type
ctypes.cast("abc", ctypes.py_object).ob_size
ctypes.cast("abc", ctypes.py_object).ob_shash
ctypes.cast("abc", ctypes.py_object).ob_sval

# Unicode is cast to PyUnicodeObject
ctypes.cast(u"abc", ctypes.py_object).ob_refcnt
ctypes.cast(u
