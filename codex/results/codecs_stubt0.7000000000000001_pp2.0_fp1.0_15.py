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

# Note that we test with surrogate pairs in the input, even if the
# codec doesn't support surrogates, because that's what happens if you
# decode a non-well-formed UTF-16 sequence.

def check_surrogates(codec):
    # Produce surrogates by decoding a non-well-formed UTF-16 sequence
    s = b'\xff\xff\xff\xff'
    if codec == "utf-8":
        s = s.decode("utf-16-be")
    if codec == "utf-16":
        s = b'\xff\xff\xff\xff'
    if codec == "utf-32":
        s = b'\xff\xff\xff\xff'
    try:
        s.decode(codec)
    except UnicodeDecodeError as e:
        # Assert that the surrogates are in the replacement string.
        # (They're in reverse order to what we're used to seeing.)
        assert e.object[e.start:e.end] == b'\xed\xa0\x80\xed\
