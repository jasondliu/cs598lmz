import ctypes
ctypes.cast(0, ctypes.py_object)

#>>> ctypes.cast(0, ctypes.py_object)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/usr/lib/python2.7/ctypes/__init__.py", line 373, in cast
#    return _cast(obj, _type)
#TypeError: int() argument must be a string or a number, not 'NoneType'

#>>> ctypes.cast(0, ctypes.py_object)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/usr/lib/python2.7/ctypes/__init__.py", line 373, in cast
#    return _cast(obj, _type)
#TypeError: int() argument must be a string or a number, not 'NoneType'

#>>> ctypes.cast(0, ctypes.py_object)
#Traceback (most recent call last):
#  File "<
