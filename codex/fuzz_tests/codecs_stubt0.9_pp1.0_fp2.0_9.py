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

def check_error_for_encoding(encoding):
    name = "ignore" if encoding.lower() == 'utf-16' else "add_utf16_bytes"
    e1 = codecs.getencoder(encoding)
    e2, _ = codecs.getencoder(encoding+'_error')

    # utf-16 does not support surrogates, so it will not be converted
    # to a single codepoint when the error handler is set to "ignore"
    if name == "ignore":
        assert e1("a\ud800b") == e2("a\ud800b", name)
        assert e1("a\udfffb") == e2("a\udfffb", name)

    # code unit at 0xFFFF can't converted to a valid UTF-16 code unit
    assert e1("\ud800") != e2("\ud800", name)

    # we can't add 3rd UTF-16 surrogate, but we have to add some surrogate
    assert e1("\ud800\ud800\ud800") != e2("\ud
