import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.notanencoding', bad_encode)
codecs.register_error('test.notadecoding', bad_decode)

def test_decode(encoding):
    try:
        u'\u3042'.encode(encoding)
    except LookupError:
        pass
    else:
        raise Exception("encoding %s should not be supported" % encoding)

def test_encode(encoding):
    try:
        u'\u3042'.encode(encoding)
    except LookupError:
        pass
    else:
        raise Exception("encoding %s should not be supported" % encoding)

test_encode('test.notanencoding')
test_decode('test.notanencoding')
test_encode('test.notadecoding')
