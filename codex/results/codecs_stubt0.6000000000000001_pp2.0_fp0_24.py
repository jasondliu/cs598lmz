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

def test_utf8_decode():
    for input, expected in [
        (b'\xe4', "ä"),
        (b'\xe4\xe4', "ää"),
        (b'\xe4\xe4\xe4', "äää"),
        (b'\xe4\xe4\xe4\xe4', "ääää"),
        (b'\xe4\xe4\xe4\xe4\xe4', "äääää"),
        (b'\xed\xa0\x80', "\ud800"), # surrogate pair (high surrogate)
        (b'\xed\xa0\x80\xed\xb0\x80', "\ud800\udc00"), # surrogate pair (high and low surrogate)
        (b'\xed\xa0\x80\xed\xb0\x80\xed\xa0\x80', "\ud800\udc00\ud800"), # surrogate pair (high and low surrogate and high surrogate)
        (b'\xf4\x8f\
