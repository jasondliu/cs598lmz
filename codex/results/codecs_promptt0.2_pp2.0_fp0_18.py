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

def test_register_error():
    # Test codecs.register_error
    codecs.register_error("test.bad_decode", bad_decode_handler)
    codecs.register_error("test.bad_encode", bad_encode_handler)
    codecs.register_error("test.bad_decode", None)
    codecs.register_error("test.bad_encode", None)
    codecs.register_error("test.bad_decode", bad_decode_handler)
    codecs.register_error("test.bad_encode",
