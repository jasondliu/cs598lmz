import ctypes
# Test ctypes.CFUNCTYPE
def f(x):
    return 2*x

g = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)
assert g(2) == 4
# Test ctypes.POINTER
g2 = ctypes.POINTER(ctypes.c_int)
assert g == g2(g)
# Test ctypes.CDLL
C_LIB = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'c_lib.so'))
assert C_LIB.reverse("123") == "321"
# Test ctypes.PYFUNCTYPE
@PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
def g3(x):
    return x**2

assert C_LIB.test_pyfunc(g3) == g3(10)
# Test ctypes.CArgObject
assert C_LIB.test_cargobject(g3) == g3(10)
# Test ctypes.py_object
assert C_LIB.
