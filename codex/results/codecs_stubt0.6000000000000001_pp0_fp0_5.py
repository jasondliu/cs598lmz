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

def test_one_codepoint(msg, func):
    try:
        func()
        raise RuntimeError("no error")
    except UnicodeDecodeError as exc:
        assert exc.args[0] == msg, exc.args[0]
        assert exc.args[2] == 3, exc.args[2]
        assert exc.args[3] == 3, exc.args[3]
        assert exc.args[4] == "add_one_codepoint", exc.args[4]

def test_utf16_bytes(msg, func):
    try:
        func()
        raise RuntimeError("no error")
    except UnicodeDecodeError as exc:
        assert exc.args[0] == msg, exc.args[0]
        assert exc.args[2] == 2, exc.args[2]
        assert exc.args[3] == 2, exc.args[3]
        assert exc.args[4] == "add_utf16_bytes", exc.args[4]

def test_utf32_bytes(msg, func):

