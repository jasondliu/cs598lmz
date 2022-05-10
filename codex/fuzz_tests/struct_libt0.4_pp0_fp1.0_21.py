import _struct

#
# Constants
#

#
# Types
#

#
# Functions
#

#
# Classes
#

class _Py_NotImplementedStruct(Structure):
    """
    Structure used to represent the C-level Py_NotImplemented.
    """
    _fields_ = [
        ('ob_refcnt', c_size_t),
        ('ob_type', c_void_p),
    ]

Py_NotImplemented = _Py_NotImplementedStruct.in_dll(
    _ctypes.pythonapi, 'Py_NotImplemented')

#
# Functions
#

def is_not_implemented(obj):
    """
    is_not_implemented(obj) -> bool

    Return True if obj is the C-level Py_NotImplemented object.
    """
    return bool(obj is Py_NotImplemented)


def not_implemented():
    """
    not_implemented() -> NotImplemented

    Return the NotImplemented
