import ctypes
ctypes.cast(0, ctypes.py_object).value

>>> import ctypes
>>> ctypes.cast(0, ctypes.py_object).value
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ctypes.cast(0, ctypes.py_object).value
ValueError: NULL pointer access

>>> from ctypes import py_object, cast
>>> cast(0, py_object).value
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    cast(0, py_object).value
ValueError: NULL pointer access
"""

import sys

def _test():
    import doctest
    doctest.testmod()
    print "testing 'FunctionType'..."
    if not hasattr(sys, 'gettotalrefcount'):
        print >> sys.stderr, "WARNING: cannot test leak detection"
    else:
        import ffi_test
        ffi_test.check(sys.gettotalrefcount())
    print "done
