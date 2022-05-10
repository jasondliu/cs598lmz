import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_none():
    assert fun() is None

def test_none_as_int():
    assert int(None) == 0
    assert None == 0
    assert None >= 0
    assert None <= 0
    assert None < 1
    assert None > -1

def test_none_as_float():
    assert float(None) == 0.0
    assert None == 0.0
    assert None >= 0.0
    assert None <= 0.0
    assert None < 1.0
    assert None > -1.0

def test_none_as_bool():
    assert not None
    assert int(not None) == 1

def test_none_as_string():
    assert str(None) == "None"
    assert repr(None) == "None"

def test_none_as_list():
    assert list(None) == []

def test_none_as_tuple():
    assert tuple(None) == ()

def test_none_as_dict():
    assert dict(None) == {}

def test
