import codecs
# Test codecs.register_error

def test_register_error():
    # Test registering an error handler
    # First, try to register an error handler for an unknown codec
    try:
        codecs.register_error("my_error_handler", None)
    except LookupError:
        pass
    else:
        raise TestFailed, "shouldn't be able to register error handler for unknown codec"

    # Now, try to register an error handler for a known codec
    try:
        codecs.register_error("my_error_handler", codecs.strict_errors)
    except LookupError:
        raise TestFailed, "should be able to register error handler for known codec"
    else:
        # Try to get the error handler
        try:
            codecs.lookup_error("my_error_handler")
        except LookupError:
            raise TestFailed, "should be able to lookup error handler"
        else:
            # Try to get the error handler for an unknown error handler
            try:
                codecs.lookup_error("unknown_error_handler")
            except Lookup
