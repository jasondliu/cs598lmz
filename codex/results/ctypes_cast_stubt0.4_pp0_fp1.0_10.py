import ctypes
ctypes.cast(0, ctypes.py_object).value

# The following code does not work in Python 2.6
#ctypes.cast(0, ctypes.py_object).value
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: NULL pointer access

# In Python 2.6, you can use from_address() instead of cast()
ctypes.py_object.from_address(0).value
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: NULL pointer access

# In Python 2.6, you can use from_address() instead of cast()
ctypes.py_object.from_address(0).value
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: NULL pointer access

# In Python 2.6, you can use from_address() instead of cast()
ctypes.py_object.from_address(0).value
#Trace
