import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad_decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad_encode"

def bad_decode_handler(exception):
    return (u"\ufffd", exception.end)

def bad_encode_handler(exception):
    return (u"\ufffd", exception.end)

def test_bad_decode():
    codecs.register_error("test.bad_decode", bad_decode_handler)
    codecs.register_error("test.bad_encode", bad_encode_handler)
    codecs.register(bad_decode)
    codecs.register(bad_encode)
    s = "abc\x80\x80\xc0\x80def"
    u = u"abc\ufffd\ufffd\ufffddef"
    assert unicode(s, "test.bad_decode") == u
    assert
