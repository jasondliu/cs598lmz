import codecs
# Test codecs.register_error()

def test_register_error():
    # SF bug #1224169: Registering a new error handler failed.
    codecs.register_error("test.ignore", codecs.ignore_errors)
    codecs.register_error("test.ignore", codecs.ignore_errors)

def test_register_error_unicode():
    # SF bug #1224169: Registering a new error handler failed.
    codecs.register_error(u"test.ignore", codecs.ignore_errors)
    codecs.register_error(u"test.ignore", codecs.ignore_errors)

def test_register_error_unicode_name():
    # SF bug #1224169: Registering a new error handler failed.
    codecs.register_error("test.ignore", codecs.ignore_errors)
    codecs.register_error(u"test.ignore", codecs.ignore_errors)

def test_noncallable():
    # SF bug #1224169: Registering a new error handler failed.
    def f():
        codecs.register_
