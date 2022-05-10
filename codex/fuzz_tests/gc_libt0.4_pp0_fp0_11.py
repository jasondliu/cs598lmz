import gc, weakref
from ctypes import *

class PyObject(Structure):
    pass

PyObject._fields_ = [
    ('ob_refcnt', c_size_t),
    ('ob_type',   c_void_p)
]

class PyVarObject(Structure):
    pass

PyVarObject._fields_ = [
    ('ob_refcnt', c_size_t),
    ('ob_type',   c_void_p),
    ('ob_size',   c_size_t)
]

class PyIntObject(Structure):
    pass

PyIntObject._fields_ = [
    ('ob_refcnt', c_size_t),
    ('ob_type',   c_void_p),
    ('ob_ival',   c_long)
]

class PyStringObject(Structure):
    pass

PyStringObject._fields_ = [
    ('ob_refcnt', c_size_t),
    ('ob_type',   c_void_p),
    ('ob_size',   c_size
