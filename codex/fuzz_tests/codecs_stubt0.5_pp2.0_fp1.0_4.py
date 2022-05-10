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

def test(enc, s):
    print("%s: %a" % (enc, s))
    e = s.encode(enc, "replace")
    print("%s (replace): %a" % (enc, e))
    d = e.decode(enc, "replace")
    print("%s (replace): %a" % (enc, d))
    e = s.encode(enc, "ignore")
    print("%s (ignore): %a" % (enc, e))
    d = e.decode(enc, "ignore")
    print("%s (ignore): %a" % (enc, d))
    e = s.encode(enc, "xmlcharrefreplace")
    print("%s (xmlcharrefreplace): %a" % (enc, e))
    d = e.decode(enc, "xmlcharrefreplace")
    print("%s (xmlcharrefreplace): %a" % (enc, d))
    e = s.encode(enc, "backslashreplace")
    print("%s (backsl
