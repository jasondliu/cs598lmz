import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
print(FUNTYPE(42))

# ctypes.py_object
# ctypes.py_object is a special type, that allows you to pass a Python object as void pointer.
# This is useful to pass Python objects to callbacks.

# ctypes.py_object is a special type, that allows you to pass a Python object as void pointer.
# This is useful to pass Python objects to callbacks.
#
# To use ctypes.py_object, you must import the Python/C API module, and use the Py_INCREF and Py_DECREF
# macros to increment and decrement the reference count of the object, respectively.
#
# Here is an example of using ctypes.py_object to pass a Python object to a callback function:

import sys
import ctypes

if sys.version_info[0] >= 3:
    import _testcapi
    Py_ssize_t = ctypes.c_ssize_t
else:
    import _testcapi as _testcapi
    Py_ssize_
