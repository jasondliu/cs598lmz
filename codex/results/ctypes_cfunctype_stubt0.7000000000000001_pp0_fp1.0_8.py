import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "xyz"

PyCode_New = ctypes.pythonapi.PyCode_New
PyCode_New.restype = ctypes.py_object
PyCode_New.argtypes = [
    ctypes.c_int,           # int argcount
    ctypes.c_int,           # int nlocals
    ctypes.c_int,           # int stacksize
    ctypes.c_int,           # int flags
    ctypes.py_object,       # PyObject *code
    ctypes.py_object,       # PyObject *consts
    ctypes.py_object,       # PyObject *names
    ctypes.py_object,       # PyObject *varnames
    ctypes.py_object,       # PyObject *freevars
    ctypes.py_object,       # PyObject *cellvars
    ctypes.py_object,       # PyObject *filename
    ctypes.py_object,       # PyObject *name
    ctypes.c_int,           # int firstlineno
    ctypes.py_object,
