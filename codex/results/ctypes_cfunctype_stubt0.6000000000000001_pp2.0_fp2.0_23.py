import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return object()

try:
    ctypes.pythonapi.Py_InitModule4
except AttributeError:
    print("Py_InitModule4 not present")
else:
    Py_InitModule4 = ctypes.pythonapi.Py_InitModule4
    Py_InitModule4.argtypes = [
        ctypes.c_char_p,
        ctypes.POINTER(PyMethodDef),
        ctypes.c_char_p,
        ctypes.py_object,
        ctypes.c_int]
    Py_InitModule4.restype = ctypes.py_object

    Py_InitModule4(b"spam", methods, b"spam module", None, PYTHON_API_VERSION)
    import spam
    assert spam.fun() is None
    del spam, Py_InitModule4

# Check with a module dict
import sys
m = {}
Py_InitModule4(b"spam", methods, b"spam module", m, PYTHON_API_VERSION)
import spam
assert spam.fun() is None

