import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_typedef():
    imp = get_python_api()[0]
    engine = JSEngine()
    engine.eval("""
        var test = {};
        test.foo = function(x, y) { return x + y; }
    """)

    py_s = imp.PyTypeObjectPtr.from_param(ctypes.c_int.__ctype_be__)
    ct = get_python_api()[0].PyType_Type.from_param(ctypes.c_int.__ctype_be__)

if __name__ == '__main__':
    engine = JSEngine()
    status = engine.eval(sys.stdin.read())
    if status is None:
        sys.stderr.write(str(engine.lastException)+'\n')
        sys.exit(1)
