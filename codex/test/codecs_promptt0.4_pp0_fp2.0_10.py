import codecs
# Test codecs.register_error()

def test_register_error():
    # Test registering a custom error handler
    def my_error_handler(exception):
        return (u'', exception.end)
    codecs.register_error('test.my_error_handler', my_error_handler)
    assert codecs.lookup_error('test.my_error_handler') is my_error_handler
    # Test registering a custom error handler as a string
    codecs.register_error('test.my_error_handler2', 'test.my_error_handler')
    assert codecs.lookup_error('test.my_error_handler2') is my_error_handler
    # Test registering a non-existing error handler
    raises(LookupError, codecs.register_error, 'test.my_error_handler3',
           'test.my_error_handler4')
    # Test registering an existing error handler
    raises(TypeError, codecs.register_error, 'test.my_error_handler',
           my_error_handler)
    # Test registering a non-callable error handler
