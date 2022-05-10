import _struct
# Test _struct.Struct
with subTest(name='pack'):
    func = _struct.Struct('!i').pack
    assert func(42) == b'*\x00\x00\x00'
with subTest(name='unpack'):
    func = _struct.Struct('!i').unpack
    assert func(b'*\x00\x00\x00') == (42,)
with subTest(name='calcsize'):
    func = _struct.Struct('!i').calcsize
    assert func() == 4
with subTest(name='format'):
    func = _struct.Struct('!i').format
    assert func() == '!i'

# Test group
with group('are_str_and_bytes_equal'):
    from . import py3_are_str_and_bytes_equal
    with subTest(name='str and bytes'):
        assert py3_are_str_and_bytes_equal(b'', '')
        assert py3_are_str_and_bytes_equal(b'foo', 'foo')
    with sub
