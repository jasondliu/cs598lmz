import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

def test_call_python():
    assert fun() == 5

def test_call_python_error():
    import ctypes
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def fun():
        return 5/0

    try:
        fun()
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError

def test_call_python_error2():
    import ctypes
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def fun():
        raise ValueError
    try:
        fun()
    except ValueError:
        pass
    else:
        raise AssertionError

def test_call_python_error3():
    import ctypes
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def fun():
        raise ValueError
    try:
        fun()
    except ZeroDivisionError:
        raise
