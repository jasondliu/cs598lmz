import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_int():
    assert ctypes.cast(ctypes.c_int(42), ctypes.py_object) == 42

def test_str():
    assert ctypes.cast(ctypes.c_char_p(b"hello"), ctypes.py_object) == "hello"

def test_unichar():
    assert ctypes.cast(ctypes.c_wchar(u'\u1234'), ctypes.py_object) == u'\u1234'

def test_unistr():
    assert ctypes.cast(ctypes.c_wchar_p(u"hello"), ctypes.py_object) == u"hello"

def test_buffer():
    assert ctypes.cast(ctypes.create_string_buffer(b"hello"), ctypes.py_object) == b"hello"

