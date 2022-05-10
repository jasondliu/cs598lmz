import codecs
# Test codecs.register_error()
def test_register_error():
    # Test that we can register a new error handler
    codecs.register_error("test.strict", codecs.strict_errors)
    codecs.register_error("test.ignore", codecs.ignore_errors)
    codecs.register_error("test.replace", codecs.replace_errors)
    codecs.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
    codecs.register_error("test.backslashreplace", codecs.backslashreplace_errors)
    # Test that we can look up the error handler by name
    codecs.lookup_error("test.strict")
    codecs.lookup_error("test.ignore")
    codecs.lookup_error("test.replace")
    codecs.lookup_error("test.xmlcharrefreplace")
    codecs.lookup_error("test.backslashreplace")
    # Test that we can encode with the error handler
    u"abc".encode("ascii", "test.st
