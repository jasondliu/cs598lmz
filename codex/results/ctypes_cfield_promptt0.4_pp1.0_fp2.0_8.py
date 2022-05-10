import ctypes
# Test ctypes.CField
#
# Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> class POINT(ctypes.Structure):
# ...     _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
# ...
# >>> point = POINT()
# >>> point.x = 2
# >>> point.y = 3
# >>> point.x
# 2
# >>> point.y
# 3
# >>> point.x = 'a'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be integer, not str
# >>> point.x = None
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be integer, not NoneType
# >>> point.x = 2.0
#
