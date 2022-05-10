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
compile_and_import(C_SOURCE_TEMPLATE)
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
fun = FUNTYPE(("fun", testlib.libtest))
ret = fun()
assert ret == 42

# Test return long

del fun
C_SOURCE_TEMPLATE = """
PyObject* fun() {
  return Py_BuildValue("l", 42L);
}
"""
compile_and_import(C_SOURCE_TEMPLATE)
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
fun = FUNTYPE(("fun", testlib.libtest))
ret = fun()
assert ret == 42L

# Test return float

del fun
C_SOURCE_TEMPLATE = """
Py
