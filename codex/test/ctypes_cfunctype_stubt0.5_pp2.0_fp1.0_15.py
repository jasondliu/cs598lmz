import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b'hello world'

def test():
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
    assert isinstance(f, bytes)
    assert f == b'hello world'
    f = fun()
