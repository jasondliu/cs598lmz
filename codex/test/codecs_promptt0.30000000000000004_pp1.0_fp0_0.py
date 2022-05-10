import codecs
# Test codecs.register_error

def test_register_error():
    def my_replace(exc):
        if isinstance(exc, UnicodeDecodeError):
            return (u'\ufffd', exc.end)
        else:
            raise TypeError("don't know how to handle %r" % exc)

    codecs.register_error("my_replace", my_replace)
    assert codecs.lookup_error("my_replace") is my_replace
    assert codecs.lookup_error("my_replace")(UnicodeDecodeError("ascii", "\xff", 0, 1, "ouch")) == (u'\ufffd', 1)
    assert codecs.lookup_error("my_replace")(UnicodeEncodeError("ascii", u"\u1234", 0, 1, "ouch")) == (u'\ufffd', 1)
    raises(TypeError, codecs.lookup_error("my_replace"), UnicodeError("ouch"))
    raises(LookupError, codecs.lookup_error, "xxx")
