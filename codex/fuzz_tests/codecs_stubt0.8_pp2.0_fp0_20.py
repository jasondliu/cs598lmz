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

for encoding in ("utf-8", "utf-16", "utf-32"):
    # 'utf-16' and 'utf-32' only accept 2 or 4 byte strings
    encoder = codecs.getincrementalencoder(encoding)("replace")
    assert encoder.errors == "replace"
    assert encoder.encode("abc") == "abc"
    encoder.reset()

    encoder = codecs.getincrementalencoder(encoding)("ignore")
    assert encoder.errors == "ignore"
    assert encoder.encode("abc") == "abc"
    encoder.reset()

    encoder = codecs.getincrementalencoder(encoding)("xmlcharrefreplace")
    assert encoder.errors == "xmlcharrefreplace"
    assert encoder.encode("abc") == "abc"
    encoder.reset()

    encoder = codecs.getincrementalencoder(encoding)("backslashreplace")
    assert encoder.errors == "backslashreplace"
    assert encoder.encode("abc")
