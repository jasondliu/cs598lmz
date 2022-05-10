import codecs
# Test codecs.register_error

def test_register_error():
    import codecs, encodings.aliases

    def x_replace(exc):
        if isinstance(exc, UnicodeError):
            return (u'\ufffd', exc.end)
        else:
            raise TypeError("don't know how to handle %r" % exc)

    codecs.register_error("test.x_replace", x_replace)
    assert codecs.lookup_error("test.x_replace") is x_replace
    assert codecs.lookup_error("test.x_replace") is x_replace
    assert encodings.aliases.aliases["test.x_replace"] == "test.x_replace"
    raises(KeyError, codecs.lookup_error, "test.x_replace_nonexisting")
    raises(KeyError, codecs.lookup_error, "test.x_replace_nonexisting")
    raises(KeyError, "encodings.aliases.aliases['test.x_replace_nonexisting']")

