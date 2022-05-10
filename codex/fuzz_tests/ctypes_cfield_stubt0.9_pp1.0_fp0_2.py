import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_byref_arg(CArg):
    code = compile("signed char b[5]; f(byref(b));", "<test>", "exec")
    d = {}
    exec(code, d)
    f = d['f']
    f.argtypes = [CArg]
    try:
        f(None)
    except TypeError:
        pass
    else:
        raise Exception("this should have raised TypeError")

def test_byref_ret(CArg):
    code = compile("signed char b[5]; x = f(b);", "<test>", "exec")
    d = {}
    exec(code, d)
    f = d['f']
    f.restype = CArg
    try:
        f(None)
    except TypeError:
        pass
    else:
        raise Exception("this should have raised TypeError")

def test_byref_arg_cast(CArg):
    code = compile("signed char b[5]; f(py_object(b));", "<test>", "exec")

