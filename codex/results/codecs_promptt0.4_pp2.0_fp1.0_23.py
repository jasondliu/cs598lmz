import codecs
# Test codecs.register_error

def test_register_error():
    import codecs
    def bad_handler(exception):
        raise TypeError("bad handler")
    codecs.register_error("test.bad_handler", bad_handler)
    try:
        codecs.lookup_error("test.bad_handler")
    except LookupError:
        pass
    else:
        raise TestFailed("lookup_error didn't raise LookupError")
    codecs.register_error("test.bad_handler", None)
    #
    def bad_handler(exception):
        raise TypeError("bad handler")
    codecs.register_error("test.bad_handler", bad_handler)
    try:
        codecs.lookup_error("test.bad_handler")
    except TypeError:
        pass
    else:
        raise TestFailed("lookup_error didn't raise TypeError")
    codecs.register_error("test.bad_handler", None)
    #
    def bad_handler(exception):
        raise AttributeError("bad handler")
    codec
