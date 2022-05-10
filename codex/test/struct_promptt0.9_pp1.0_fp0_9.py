import _struct
# Test _struct.Struct
def test_Struct_setattr():
    def check(tp):
        s = _struct.Struct(tp)
        try:
            s.format
        except AttributeError:
            pass
        else:
            assert False, tp
        try:
            s.size
        except AttributeError:
            pass
        else:
            assert False, tp
        try:
            s.alignment
        except AttributeError:
            pass
        else:
            assert False, tp
    check('l')
    check('90x')
    check('30p')


def test_Struct_basics():
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('i').alignment == 4
    assert _struct.Struct('p').size == _struct.calcsize('p')
    assert _struct.Struct('p').alignment == _struct.calcsize('p')
    assert _struct.Struct('l').size == _struct.calcsize('l')
    assert _struct.Struct('l').alignment == _struct.cal
