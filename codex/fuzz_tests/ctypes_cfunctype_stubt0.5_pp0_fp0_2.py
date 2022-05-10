import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_ctypes_function_returns_bytes():
    assert fun() == b"hello"

def test_ctypes_function_returns_unicode():
    assert fun() == u"hello"

@FUNTYPE
def fun2():
    return b"hello"

def test_ctypes_function_returns_bytes_bytes():
    assert fun2() == b"hello"

def test_ctypes_function_returns_bytes_unicode():
    assert fun2() == u"hello"

@FUNTYPE
def fun3():
    return u"hello"

def test_ctypes_function_returns_unicode_bytes():
    assert fun3() == b"hello"

def test_ctypes_function_returns_unicode_unicode():
    assert fun3() == u"hello"

def test_ctypes_function_with_bytes_returns_bytes():
    assert fun(b"hello") == b"hello"

def test_ctypes_function_with_bytes_returns
