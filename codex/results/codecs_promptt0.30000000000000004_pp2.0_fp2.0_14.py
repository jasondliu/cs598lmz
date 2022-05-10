import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad", input, 0, 1, "bad")

def bad_translate(input, errors='strict'):
    raise UnicodeTranslateError(input, 0, 1, "bad")

codecs.register_error("test.bad_decode", bad_decode)
codecs.register_error("test.bad_encode", bad_encode)
codecs.register_error("test.bad_translate", bad_translate)

# Test codecs.lookup_error

def test_lookup_error(name):
    try:
        codecs.lookup_error(name)
    except LookupError:
        pass
    else:
        raise Exception("lookup_error didn't raise LookupError")

test_lookup_error("test.bad_decode")
test_
