import codecs
# Test codecs.register_error

def test_register_error():
    # Test registering an error handler
    # First, we need an encoding that doesn't exist
    try:
        codecs.lookup("__spam__")
    except LookupError:
        pass
    else:
        raise TestFailed("encoding '__spam__' should not exist")
    # Now register an error handler for it
    def my_error_handler(exception):
        if isinstance(exception, UnicodeEncodeError):
            x, y = exception.object[exception.start:exception.end], exception.end
            return (u"<%s>" % x, y)
        elif isinstance(exception, UnicodeDecodeError):
            x, y = exception.object[exception.start:exception.end], exception.end
            return (u"<%s>" % x, y)
        elif isinstance(exception, UnicodeTranslateError):
            x, y = exception.object[exception.start:exception.end], exception.end
