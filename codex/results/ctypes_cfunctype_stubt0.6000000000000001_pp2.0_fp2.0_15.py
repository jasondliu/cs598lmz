import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5
print fun()
</code>
I've tried this and it works, but I don't understand why. <code>ctypes.py_object</code> is a pointer to <code>PyObject</code> struct in Python.h:
<code>typedef struct _object {
    PyObject_HEAD
} PyObject;
</code>
I think I'm missing some important point.

