import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class PyObject(ctypes.Structure):
    pass

PyObject._fields_ = [("ob_refcnt", ctypes.c_ssize_t),
                     ("ob_type", ctypes.POINTER(PyObject))]

class PyVarObject(PyObject):
    pass

PyVarObject._fields_ = [("ob_size", ctypes.c_ssize_t)]

class PyTypeObject(PyVarObject):
    _fields_ = [("tp_name", ctypes.c_char_p)]

PyObject.ob_type.__doc__ = "Public fields must have valid docstrings"

assert PyObject.ob_type.__doc__ == "Public fields must have valid docstrings"
assert PyObject.ob_type._field_type_ == "P"
assert PyObject.ob_type._ctype_ == ctypes.POINTER(PyObject)
assert PyObject.ob_refcnt.__doc__ == "Public fields must have valid docstrings"
assert PyObject.ob_refcnt._field_type_ == "l"
