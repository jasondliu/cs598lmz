import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    return (u'', len(input))

def bad_encode(input, errors='strict'):
    return (u'', len(input))

codecs.register_error('test.bad', bad_decode)

def test_decode():
    assert codecs.lookup_error('test.bad') is bad_decode
    assert codecs.lookup_error('test.bad_encode') is None
    assert codecs.lookup_error('bad_encode') is None
    assert codecs.lookup_error('bad') is None

def test_encode():
    assert codecs.lookup_error('test.bad_encode') is None
    assert codecs.lookup_error('test.bad') is bad_decode
    assert codecs.lookup_error('bad_encode') is None
    assert codecs.lookup_error('bad') is None

