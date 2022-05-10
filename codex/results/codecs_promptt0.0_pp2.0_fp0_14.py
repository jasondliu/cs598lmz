import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test_bad_decode():
    try:
        u"abc".encode("ascii", "test.bad_decode")
    except UnicodeError, err:
        assert str(err) == "bad decode"
    else:
        raise AssertionError, "should have raised UnicodeError"

def test_bad_encode():
    try:
        u"abc".encode("ascii", "test.bad_encode")
    except UnicodeError, err:
        assert str(err) == "bad encode"
    else:
        raise AssertionError, "should have raised UnicodeError"

def test_bad_
