import ctypes
# Test ctypes.CFUNCTYPE(...)
cfunc = ctypes.CFUNCTYPE(ctypes.c_int)((lambda x: x % 2))
# Test C function
cpy = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libtest.so'))
def CheckPyFunc(func, *args):
    return func(*args)
def CheckCFunction(func, *args):
    return cpy.PyObject_CallFunction(func, *args)
# Test method
# Note that the library won't free the reference
class PyObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_int),
                ("ob_type", ctypes.c_void_p)]
class PyTypeObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_int),
                ("ob_type", ctypes.c_void_p),
                ("tp_name", ctypes.c_char_p)]
class Py
