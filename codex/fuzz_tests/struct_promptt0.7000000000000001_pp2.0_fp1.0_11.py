import _struct
# Test _struct.Struct.__new__, __getinitargs__, __setstate__, __reduce__
# and __reduce_ex__

def test_new():
    def f(format):
        s = _struct.Struct(format)
        assert type(s) is _struct.Struct
        return s
    for format in ('x', 'cb', 'hhi', 'l', 'q', 'P'):
        f(format)
    raises(TypeError, f, 1)
    raises(TypeError, f, 'hhhhi')
    raises(TypeError, f, 'hij')
    raises(TypeError, f, '')
    raises(TypeError, f, 'yy')
    raises(TypeError, f, '@i')
    raises(TypeError, f, '!i')
    raises(TypeError, f, '<i')
    raises(TypeError, f, '>i')
    raises(TypeError, f, '^i')
    raises(TypeError, f, '=i')
    raises(TypeError, f, '!ih')
    raises(
