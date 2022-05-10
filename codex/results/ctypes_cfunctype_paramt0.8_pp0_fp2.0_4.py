import ctypes
FUNTYPE = ctypes.CFUNCTYPE(c_double, c_double)
def makeufunc(code):
    c_getarray = get_c_array(code, 1)
    CALL_GETARRAY = FUNTYPE(c_getarray)
    def f(v):
        return CALL_GETARRAY(v)
    return f

class GetArrayTest(unittest.TestCase):
    def test(self):
        self._check('''
        int getarray(double x) { return x; }
        ''', ((0.0, 0.0), (1.0, 1.0), (-2.0, -2.0), (3.0, 3.0), (5.5, 5.5)))

    def test_with_macro(self):
        self._check('''
        #define PLUS_ONE(x) ((x)+(1))
        int getarray(double x) { return PLUS_ONE(x); }
        ''', ((0.0, 1.0), (1.0, 2.0), (-2.0, -1.0), (3.0,
