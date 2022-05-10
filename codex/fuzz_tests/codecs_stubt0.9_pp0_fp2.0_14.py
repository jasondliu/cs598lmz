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

def encdec(encoder, decoder, input, errors=None):
    if errors is None:
        errors = "strict"
    encoded = encoder(input, errors)[0]
    decoded = decoder(encoded, errors)[0]
    return (input, encoded, decoded)

def test(input, **kwargs):
    return encdec(unicode.encode, unicode.decode, input, **kwargs)

input = "abc"

tests = [
    ("ascii", test("abc")),
    ("ascii replace", test("\x00\xff", "replace")),
    ("ascii ignore", test("\x00\xff", "ignore")),
    ("latin9 replace", test("\x01\xfe", "latin_1")),
    ("latin9 ignore", test("\x01\xfe", "latin_1", "ignore")),
    ("utf8 strict", test("\u0100\uffff")),
    ("utf8 replace", test("\x00\xff\u
