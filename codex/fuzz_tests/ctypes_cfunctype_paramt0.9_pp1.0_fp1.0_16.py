import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def pyfunc(arg):
    ctypes.pythonapi.PyTraceBack_Here(ctypes.c_int(2))
    return arg + 42
def test_traceback_funcaddr(lib):
    pyfunc = pyfunc
    f = FUNTYPE(pyfunc)
    funcaddr = ctypes.cast(f, ctypes.c_void_p).value
    pyfunc = None
    C = ctypes.CDLL(ctypes.util.find_library('c'))
    C.raise_exception.restype = ctypes.c_int
    raises(Exception, C.raise_exception)
    err = C.get_error()
    import os.path
    filename = os.path.normcase(__file__)
    assert err == ('File "%s", line 8, in pyfunc\n' % filename)


def test_funcaddress_returns_int():
    from ctypes import CDLL, addressof
    C = CDLL(ctypes.util.find_library('
