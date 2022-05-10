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

# --- Tests

def test_encode_surrogate():
    "test encoding with error handling"
    u = '\udc80'
    for errors in ('strict', 'surrogateescape', 'surrogatepass', 'replace', 'ignore'):
        assert codecs.escape_encode(u)[0] == codecs.escape_encode(u, errors=errors)[0]

def test_encode_surrogate_pass():
    "test encoding with surrogatepass error"
    u = '\udc80'
    for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
        assert codecs.escape_encode(u, errors='surrogatepass')[0] == codecs.escape_encode(u, encoding, errors='surrogatepass')[0]

def test_encode_surrogate_in_gbk():
    "test encoding with surrogatepass error"
    u = '\udc80'
    for encoding in ('gbk', '
