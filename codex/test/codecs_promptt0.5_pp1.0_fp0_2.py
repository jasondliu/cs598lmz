import codecs
# Test codecs.register_error

def test_register_error():
    # Encoding
    codecs.register_error("strict", lambda e: (u"\ufffd", e.end))
    codecs.register_error("ignore", lambda e: (u"", e.end))
    codecs.register_error("replace", lambda e: (u"?", e.end))

    # Decoding
    codecs.register_error("strict", lambda e: (u"\ufffd", e.end))
    codecs.register_error("ignore", lambda e: (u"", e.end))
    codecs.register_error("replace", lambda e: (u"?", e.end))

    # Test error handling
    try:
        codecs.register_error("test", "foo")
    except TypeError:
        pass
