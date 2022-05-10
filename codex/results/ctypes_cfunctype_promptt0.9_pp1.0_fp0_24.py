import ctypes
# Test ctypes.CFUNCTYPE()
CFUNCTYPE(c_int, c_float, c_float)
# Test PyCFUNCTYPE()
PyCFUNCTYPE(c_int, c_float, c_float)

# Test python3.2 _as_parameter_
import _ctypes
_ctypes.PyObj_FromPtr(None)

# Test ctypes.pointer_t
import ctypes._pointer_t
ctypes._pointer_t.__name__
ctypes._pointer_t
ctypes._pointer_t.__mro__
ctypes._pointer_t.__module__
ctypes._pointer_t

# Test TRY_AGAIN constant
import errno
errno.TRY_AGAIN == ctypes.TRY_AGAIN

# Test PyErr_SetImportError()
from ctypes import util
util.find_library("non_existant_library")

# Test Py_CLEAR macro
class X(object): pass
x = X()
x.obj = x
X.__del__ = lambda self: None
hash(x)
num
