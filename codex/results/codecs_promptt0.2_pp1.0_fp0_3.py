import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad", input, 0, 1, "bad")

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)

def test_decode(encoding):
    try:
        codecs.decode(b"\xff", encoding, "test.bad_decode")
    except UnicodeDecodeError as e:
        print(e)
        if e.reason != "bad":
            raise
    else:
        raise Exception("should have raised UnicodeDecodeError")

def test_encode(encoding):
    try:
        codecs.encode("\uffff", encoding, "test.bad_encode")
    except UnicodeEncodeError as e:
        print(e)
