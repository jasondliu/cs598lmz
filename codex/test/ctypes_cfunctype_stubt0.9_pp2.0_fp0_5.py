import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "test string"
ret = fun()
assert ret == "test string"

# Test return int
del fun
C_SOURCE_TEMPLATE = """
PyObject* fun() {
  return Py_BuildValue("i", 42);
}
"""
