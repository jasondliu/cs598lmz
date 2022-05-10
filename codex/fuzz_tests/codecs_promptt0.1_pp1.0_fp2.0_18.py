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
        if str(err) != "bad decode":
            raise AssertionError, "wrong exception"
    else:
        raise AssertionError, "no exception"

def test_bad_encode():
    try:
        u"abc".encode("ascii", "test.bad_encode")
    except UnicodeError, err:
        if str(err) != "bad encode":
            raise AssertionError, "wrong exception"
    else:

