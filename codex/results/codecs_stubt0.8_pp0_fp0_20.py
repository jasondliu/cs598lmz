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

def test_errors():
    u = "\xfc" # latin1: �
    utf8 = "utf8"
    utf16 = "utf-16"
    utf32 = "utf-32"

    codecs.register(lambda c: codecs.lookup(utf8) if c=="utf8-test" else None)
    codecs.register(lambda c: codecs.lookup(utf16) if c=="utf16-test" else None)
    codecs.register(lambda c: codecs.lookup(utf32) if c=="utf32-test" else None)

    tests = [
        # utf8, utf16, utf32
        (u, u, u'\xfc'),
        (u.encode(utf8), u'\xfc', u'\xfc'),
        (u.encode(utf8, "replace"), u'\ufffd', u'\xfc'),
        (u.encode(utf8, "ignore"), u'', u'\xfc'),
        (u.
