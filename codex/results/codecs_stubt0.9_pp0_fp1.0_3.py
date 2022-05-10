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

# In Python 2, the error handler was called as f(error, encoding) as well as
# f(error), but the encoding is ignored.
# In Python 3, it only calls the handler f(error).

def test_error_handler(handler):
    try:
        s.decode("ascii", handler)
    except UnicodeDecodeError as e:
        assert e.args[0] == "add_one_codepoint"
    try:
        b.decode("ascii", handler)
    except UnicodeDecodeError as e:
        assert e.args[0] == "add_utf16_bytes"
    try:
        bb.decode("ascii", handler)
    except UnicodeDecodeError as e:
        assert e.args[0] == "add_utf32_bytes"
    s = bb
    if sys.maxunicode <= 0xFFFF:
        c = b[:2]
    else:
        c = b
    try:
        s.decode("ascii", handler)
    except Unicode
