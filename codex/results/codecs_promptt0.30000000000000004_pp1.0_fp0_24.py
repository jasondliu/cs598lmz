import codecs
# Test codecs.register_error

import codecs

def test_register_error():
    def my_error_handler(exception):
        return (u'', exception.end)
    codecs.register_error('test.my_error_handler', my_error_handler)
    assert codecs.lookup_error('test.my_error_handler') is my_error_handler
    try:
        codecs.register_error('test.my_error_handler', my_error_handler)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        codecs.register_error('test.my_error_handler2', my_error_handler)
    except LookupError:
        pass
    else:
        raise AssertionError

def test_strict():
    # Test the 'strict' error handler
    def strict_error_handler(exception):
        raise exception
    codecs.register_error('test.strict', strict_error_handler)
    assert codecs.lookup_error('test.strict') is strict_
