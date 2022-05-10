import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad_decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad_encode"

def bad_decode_handler(exception):
    return (u'', exception.end)

def bad_encode_handler(exception):
    return (u'', exception.end)

def test_bad_decode():
    codecs.register_error('test.bad_decode', bad_decode_handler)
    codecs.register(bad_decode)
    try:
        u'\xff'.encode('bad_decode')
    except UnicodeError, e:
        assert str(e) == "bad_decode"
    else:
        raise AssertionError, "bad_decode didn't raise UnicodeError"

def test_bad_encode():
    codecs.register_error('test.bad_encode', bad_encode_handler)
    codecs
