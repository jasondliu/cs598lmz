import _struct
# Test _struct.Struct(format)
def test_struct_Struct():
    s = _struct.Struct('hhl')
    assert repr(s) == "Struct('hhl')"
    assert s.size == 8
    def check_error(fmt):
        try:
            _struct.Struct(fmt)
        except ValueError:
            pass
        else:
            raise AssertionError("_struct.Struct('%s') didn't fail" % fmt)
    check_error('z')
    check_error('1p')
    check_error('1s1s')
    check_error('1s2s')
    check_error('@')
    check_error('=')
    check_error('<2')
    check_error('<2x')
    check_error('<2x1s')
    check_error('<2x1s1s')
    check_error('<2x2s1s')
    check_error('<2x2s2s')
    check_error('<2x2s1a')
    check_error('<2
