import _struct
# Test _struct.Struct metaclass functions
# Verify we can replicate the 'example' cache mechanism
# Do this because even null buffers can be unpack'd

def _test_cls(c):
    x = c('float')
    y = c('float')
    assert x == x
    assert x == y
    assert x.format == y.format
    assert x.format == 'f'
    assert x.size == y.size
    assert x.size == 4

def test_default():
    _test_cls(Struct)

def test_cache():
    _test_cls(_struct.Struct)

def test_meta():
    Dummy = type('Dummy', (Struct,), {})
    base._make_trampoline(Dummy)
    _test_cls(Dummy)

def test_meta_callback():
    Dummy = type('Dummy', (Struct,), {'_set_format': lambda self: '>fff'})
    base._make_trampoline(Dummy)
    _test_cls(Dummy)

