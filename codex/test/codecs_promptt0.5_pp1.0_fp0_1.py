import codecs
# Test codecs.register_error()

import _testcapi

def test_register_error(encoding):
    # Issue #4160: test codecs.register_error()
    def handler(exception):
        print(exception)
        return ('', exception.end)
    codecs.register_error(encoding, handler)
    try:
        # Encode an unencodable character
        s = '\udc80'
        s.encode(encoding)
    finally:
        codecs.register_error(encoding, None)

def test_register_error_invalid_args(encoding):
    # Issue #4160: test codecs.register_error()
    # with invalid arguments
    with _testcapi.pytest.raises(TypeError):
        codecs.register_error(encoding, "not callable")
    with _testcapi.pytest.raises(TypeError):
        codecs.register_error("not a codec name", lambda x:x)

