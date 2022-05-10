import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class py_object(ctypes.Structure):
    pass
py_object._fields_ = [("ob_refcnt", ctypes.c_long),
                      ("ob_type", ctypes.POINTER(py_object))]

Py_ssize_t = ctypes.c_ulong

class PyStringObject(ctypes.Structure):
    pass
PyStringObject._fields_ = [("ob_refcnt", Py_ssize_t),
                           ("ob_type", ctypes.POINTER(py_object)),
                           ("ob_size", Py_ssize_t),
                           ("ob_shash", ctypes.c_long),
                           ("ob_sval", ctypes.c_char * 1)]

PyString_Type = py_object
PyString_Check = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.py_object)(
    ("PyString_Check", ctypes.pythonapi))
PyString_Check.restype = ctypes.c_long
PyString
