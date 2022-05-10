import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE = ctypes.CFUNCTYPE

def func(p):
    return p.contents.value

Py_ssize_t = ctypes.c_int

class Index(object):
    _fields_ = [('value', Py_ssize_t)]

idx = Index()

