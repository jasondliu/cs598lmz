import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

ctypes.py_object = py_object
ctypes.PyObject_HEAD = PyObject_HEAD
ctypes.Py_ssize_t = Py_ssize_t
ctypes.PyObject_VAR_HEAD = PyObject_VAR_HEAD

def new_instancemethod(func, self, klass):
    if not self:
        return func
    return types.MethodType(func, self)

types.new_instancemethod = new_instancemethod
