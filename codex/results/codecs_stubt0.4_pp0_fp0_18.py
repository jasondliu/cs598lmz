import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_main():
    # Check that UnicodeEncodeError and UnicodeDecodeError
    # have all the attributes that the codecs module expects
    for exc in (UnicodeEncodeError, UnicodeDecodeError):
        e = exc('utf-8', u"\u3042", 0, 1, "ouch")
        assert e.encoding == 'utf-8'
        assert e.object == u"\u3042"
        assert e.start == 0
        assert e.end == 1
        assert e.reason == "ouch"
        assert str(e) == "'utf-8' codec can't encode character '\\u3042' in position 0: ouch"
        assert e.__class__ == exc
        assert e.__class__.__name__ == '%s' % exc.__name__

        e = exc('utf-8', u"\u3042", 0, 1, "ouch")
        assert e.encoding == 'utf-8'
        assert e.object == u"\u3042"
        assert e.start == 0
        assert
