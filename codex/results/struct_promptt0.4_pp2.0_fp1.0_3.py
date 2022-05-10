import _struct
# Test _struct.Struct.format_size

def test_format_size():
    # Test all format codes
    for code in _struct.__dict__:
        if code[0] == '_' or code[-1] != '_':
            continue
        code = code[:-1]
        if code in 'BHILQP':
            size = _struct.Struct(code).format_size()
            assert size == _struct.calcsize(code)
        else:
            try:
                _struct.Struct(code)
            except ValueError:
                pass
            else:
                assert False, '%s: unexpected success' % code

def test_format_size_error():
    assert _struct.Struct('@').format_size() == 0
    assert _struct.Struct('@').format_size() == 0
    assert _struct.Struct('@').format_size() == 0
    assert _struct.Struct('@').format_size() == 0
    assert _struct.Struct('@').format_size() == 0
    assert _struct.Struct('@').format_size() ==
