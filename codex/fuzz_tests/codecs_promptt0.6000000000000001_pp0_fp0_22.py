import codecs
# Test codecs.register_error(
#     'test', codecs.lookup_error('surrogateescape'))

def test_decode_with_surrogateescape(data, enc):
    # Test decoding with 'surrogateescape' error handler
    u = data.decode(enc, 'surrogateescape')
    for c in u:
        if ord(c) >= 0xdc80 and ord(c) <= 0xdcff:
            assert 0xfffd != c
    s = u.encode(enc, 'surrogateescape')
    assert data == s

# Test codecs.register_error(
#     'test', codecs.lookup_error('surrogateescape'))

def test_encode_with_surrogateescape(data, enc):
    # Test encoding with 'surrogateescape' error handler
    u = data.decode(enc)
    s = u.encode(enc, 'surrogateescape')
    assert data == s

def test_register_error():
    # Testing registering new error handlers
    # Try the following with a
