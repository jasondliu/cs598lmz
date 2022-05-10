import ctypes
ctypes.cast(obj, ctypes.py_object).value

# ValueError: PyObject_AsReadBuffer called with null pointer
</code>
I'm running Python 3.3.3 on OSX 10.9.2.


A:

It looks like cx_Freeze is looking for a pointer to a <code>PyObject</code> instead of a <code>PyObject *</code>.
Since <code>ctypes</code> doesn't support a <code>PyObject</code> type, the solution is to create a type from the structure definition:
<code>from ctypes import *
from ctypes.util import find_library

# Find the Python library
libpath = find_library('python3.3')
libpython = CDLL(libpath)

# Create a type for PyObject
class PyObject(Structure):
    _fields_ = [('ob_refcnt', c_ssize_t),
                ('ob_type', py_object)]

# Create a type for the PyObject *
py_object_p = POINTER(PyObject)

# Create a PyObject *
