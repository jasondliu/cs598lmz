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

def test_unicode_error():

    # Test UnicodeError

    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        u = '\xff'
        try:
            u.encode(encoding)
            assert False
        except UnicodeEncodeError as e:
            assert e.args[2] == 1
            assert e.args[3] == 2
            assert e.args[4] == '\xff'
            assert e.object == u
            assert e.encoding == encoding
            assert str(e) == " '%s' codec can't encode character '\\xff' in position 1: %s " % (encoding, encoding.encode("ascii", "backslashreplace"))
        else:
            assert False, "should have raised"

        for err in ("strict", "replace", "ignore", "backslashreplace", "xmlcharrefreplace", "surrogateescape", "surrogatepass", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):

