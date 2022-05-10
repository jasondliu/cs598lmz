import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

def test_register_error():
    # Test registering a new error handling with codecs.register_error()
    def strict_handler(exception):
        raise exception
    codecs.register_error('strict', strict_handler)
    try:
        'abcd'.encode('ascii', 'strict')
    except UnicodeEncodeError:
        pass
    else:
        raise TestFailed('strict handler did not raise exception')

def test_ascii_decoding():
    # Test decoding of ASCII-only data
    s = 'abc\u3042\u3044\u3046\u3048\u304a'
    assert s.encode('ascii') == b'abc\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'
    assert s.encode('ascii', 'strict') == b'abc\xe3\x
