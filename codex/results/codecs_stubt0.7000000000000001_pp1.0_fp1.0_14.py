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

# --- tests

assert codecs.lookup_error("add_one_codepoint") is add_one_codepoint
assert codecs.lookup_error("add_utf16_bytes") is add_utf16_bytes
assert codecs.lookup_error("add_utf32_bytes") is add_utf32_bytes

# --- test error handling

def test_decode(encoding, input, errors, expected):
    assert codecs.decode(input, encoding, errors) == expected

def test_encode(encoding, input, errors, expected):
    assert codecs.encode(input, encoding, errors) == expected

def test_stream_writer(encoding, input, errors, expected):
    f = io.StringIO()
    w = codecs.getwriter(encoding)(f, errors=errors)
    w.write(input)
    w.flush()
    assert f.getvalue() == expected

def test_stream_reader(encoding, input, errors, expected):
    f = io.BytesIO(input)

