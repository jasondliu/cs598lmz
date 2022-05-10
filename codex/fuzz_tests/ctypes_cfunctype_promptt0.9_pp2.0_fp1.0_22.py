import ctypes
# Test ctypes.CFUNCTYPE.
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float, ctypes.c_float)(lambda f1, f2: f1
    < f2)
func(1.1, 2.0)


@pytest.mark.skipif(IS_JYTHON, reason='Marked to skip on Jython')
def test_CFUNCTYPE_decorated_function(capsys):
    # Test ctypes.CFUNCTYPE with a decorated function.
    def decorator(function):
        def wrapper(f1, f2):
            print 'test_CFUNCTYPE_decorated_function:', 'function =', function
        return wrapper

    @decorator
    def func(f1, f2):
        return f1 < f2
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float, ctypes.c_float)(func)
    func(1.1, 2.0)
    out, err = capsys.readouter
