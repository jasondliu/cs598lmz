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

def sanity_check():
    hello = u"\xe9"
    ehello = hello.encode("utf-8")
    hello2 = ehello.decode("utf-8", "strict")
    assert hello == hello2
    try:
        ehello.decode("utf-8", "unknown_error")
    except LookupError as e:
        assert "unknown error handler name 'unknown_error'" in str(e)
    else:
        raise AssertionError("did not see LookupError")
    assert ehello.decode("utf-8", "ignore") == u""
    assert ehello.decode("utf-8", "replace") == u"\ufffd"
    assert ehello.decode("utf-8", "surrogateescape") == u"\udce9"
    assert ehello.decode("utf-8", "surrogatepass") == u"\udce9"
    assert ehello.decode("utf-8", "xmlcharrefreplace") == u"&#233;"
    assert ehello.decode("
