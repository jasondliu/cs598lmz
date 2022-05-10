import _struct
# Test _struct.Struct

def assert_error(type, obj, *args):
    try:
        apply(obj, args)
    except type, err:
        pass
    else:
        print 'Expected error not raised'

def assert_bin_equal(obj, args, res):
    got = apply(obj, args)
    if got != res:
        print 'Expected', `res`
        print 'Got     ', `got`

def test_struct():
    for code in 'bBhHiIlLfd':
        fmt = code + '10p'
        s = _struct.Struct(fmt)
        if code in 'bBhH':
            assert_error(TypeError, s.pack, '', 1)
        else:
            assert_error(ValueError, s.pack, '', 1)
        assert_error(TypeError, s.pack, 1, 2, 3)
        assert_error(TypeError, s.unpack, 1)
        assert_error(TypeError, s.unpack_from, 1, 2, 3)
        assert_error
