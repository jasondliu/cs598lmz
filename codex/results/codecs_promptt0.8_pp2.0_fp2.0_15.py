import codecs
# Test codecs.register_error
# The tests are written for the surrogateescape error handler.
# The surrogatepass error handler will return an undecodable string,
# possibly with additional garbage characters.
def test_surrogateescape_decode(coding):
    # Test decoding an undecodable byte string
    s = 'ab\udc01cd\udc02'.encode(coding)
    r = codecs.decode(s, coding, 'surrogateescape')
    assert r == 'ab\udc01cd\udc02'

    # Test decoding an encoded string with a lone surrogate
    r = codecs.decode(s + '\udc03'.encode(coding), coding, 'surrogateescape')
    assert r == 'ab\udc01cd\udc02\udc03'

    # Test decoding an encoded string with an encoded lone surrogate
    r = codecs.decode(s + b'\xed\xb0\x80', coding, 'surrogateescape')
    assert r == 'ab\udc01cd\udc02\udc00'


