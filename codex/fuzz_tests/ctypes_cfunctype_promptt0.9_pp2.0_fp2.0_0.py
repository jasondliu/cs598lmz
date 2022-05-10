import ctypes
# Test ctypes.CFUNCTYPE
c_test1 = ctypes.CFUNCTYPE(ctypes.c_int)(lambda x, y: x + y)
assert c_test1(1, 2) == 3
c_test2 = ctypes.CFUNCTYPE(ctypes.c_int64)(lambda x, y: x + y)
assert c_test2(1, 2) == 3
c_test3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
assert c_test3(1, 2) == 3
c_test4 = ffi.cast("PyObject* (*)(PyObject*, PyObject*)",
                  lambda x, y: x + y)
assert c_test4("xxx", "yyy") == "xxxyyy"

@nolibc
def test_call_various_cv():
    def test(c2py, c2py_wrapped, py2c, py2c_wrapped):
        c2py0 = ctypes.
