import codecs
# Test codecs.register_error

def check_error(error, encoding, string, start, end, expected):
    try:
        u = string.decode(encoding, error)
    except UnicodeDecodeError as e:
        if (start, end, expected) != (e.start, e.end, e.reason):
            raise AssertionError("%s.decode(%r, %s) raised %s, "
                                 "but start, end and reason are wrong"
                                 % (repr(string), encoding, error, e))
    else:
        raise AssertionError("%s.decode(%r, %s) didn't raise UnicodeDecodeError"
                             % (repr(string), encoding, error))

def test_register_error():
    # Issue #1700
    class MyError(UnicodeError):
        pass

    class MyErrorHandler:
        def __init__(self, errors='strict'):
            self.errors = errors
