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

def test(msg, encode_fct, decode_fct):
    assert encode_fct(msg) == decode_fct(encode_fct(msg))
    assert encode_fct(msg, 'replace') == decode_fct(encode_fct(msg, 'replace'), 'replace')
    assert encode_fct(msg, 'ignore') == decode_fct(encode_fct(msg, 'ignore'), 'ignore')
    assert encode_fct(msg, 'xmlcharrefreplace') == decode_fct(encode_fct(msg, 'xmlcharrefreplace'), 'xmlcharrefreplace')
    # add_one_codepoint
    assert encode_fct(msg, 'add_one_codepoint') == decode_fct(encode_fct(msg, 'add_one_codepoint'), 'add_one_codepoint')
    # add_utf16_bytes
    assert encode_fct(msg, 'add_utf16_bytes') == decode_fct(encode_fct(msg, 'add_utf
