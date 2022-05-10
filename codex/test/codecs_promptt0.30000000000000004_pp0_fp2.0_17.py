import codecs
# Test codecs.register_error

def codec_error_handler(exception):
    return (u"", exception.end)

def test_register_error():
    # Encoding
    codecs.register_error("test.xmlcharrefreplace", codec_error_handler)
    codecs.register_error("test.backslashreplace", codec_error_handler)
    codecs.register_error("test.namereplace", codec_error_handler)
    # Decoding
    codecs.register_error("test.ignore", codec_error_handler)
    codecs.register_error("test.replace", codec_error_handler)
    codecs.register_error("test.xmlcharrefreplace", codec_error_handler)
    codecs.register_error("test.backslashreplace", codec_error_handler)
    codecs.register_error("test.namereplace", codec_error_handler)
    # Test that the error handlers have been registered
    assert "test.xmlcharrefreplace" in codecs.lookup_error("test.xmlcharrefreplace")
