import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue1602
#
# Python 2.6.1 (r261:67515, Dec  6 2008, 16:26:59)
# [GCC 4.0.1 (Apple Inc. build 5465)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ctypes
# >>> ctypes.cast(0, ctypes.py_object).value
# Segmentation fault
import sys
if sys.hexversion <= 0x02060000:
    import ctypes
    ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue2517
#
# Python 2.6.1 (r261:67515, Dec  6 2008, 16:26:59)
# [GCC 4.0.1 (Apple Inc. build 5465)] on
