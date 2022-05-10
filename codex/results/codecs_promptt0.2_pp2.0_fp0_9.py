import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad_decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad_encode"

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

def test_bad_decode():
    try:
        u"\xff".encode("ascii", "test.bad_decode")
    except UnicodeError, err:
        assert str(err) == "bad_decode"
    else:
        raise AssertionError, "bad_decode didn't raise UnicodeError"

def test_bad_encode():
    try:
        u"\u1234".encode("ascii", "test.bad_encode")
    except UnicodeError, err:
        assert str(err) == "bad_encode"
    else:
        raise Assertion
