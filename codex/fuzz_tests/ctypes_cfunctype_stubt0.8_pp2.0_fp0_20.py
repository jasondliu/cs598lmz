import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return rffi.r_long(1)

def test_fun():
    r = fun()
    assert r == 1
test_fun.func_annotations = {}

class TestFunc(unittest.TestCase):
    def test_func(self):
        for func in [a, b, c, d, l, m, n, o, p, q, r, s, t, u, v, w, x, y, fun]:
            check_func(func)

    def test_func_instancemethod(self):
        A = rffi.CStruct('struct A', ('x', rffi.INT))
        a = lltype.malloc(A.TO, flavor='raw')
        a.c_x = 123
        a_free = lltype.free(A, flavor='raw')
        check_func(a.c_x.__get__)
        check_func(a.c_x.__set__)
        check_func(a.c_x.__delete__)
        check_func(a_free)


