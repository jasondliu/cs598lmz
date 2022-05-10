import _struct
# Test _struct.Struct


def test_Struct1():
    s = _struct.Struct('bBhHiIlLqQfd')
    assert len(s.format) == 18
    assert s.size == 8


def test_Struct2():
    s = _struct.Struct('P')
    assert len(s.format) == 1
    assert s.size == _struct.calcsize('P')


def test_Struct3():
    s = _struct.Struct('xxxxsx')
    assert s.format == 'xxxxsx'
    assert s.size == _struct.calcsize('xxxxsx')


def test_Struct4():
    s = _struct.Struct('@')
    with pytest.raises(TypeError):
        s.pack('foo')


def test_Struct_get_set_format():
    s = _struct.Struct('b')
    with pytest.raises(TypeError):
        s.format = 1.2


def test_Struct_format_too_short():
    with pytest.raises(ValueError):
        s =
