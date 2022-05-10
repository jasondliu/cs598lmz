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

def test(b):
    try:
        b.decode('utf-8')
    except UnicodeDecodeError as exc:
        assert exc.args[2] == 1

    try:
        b.decode('utf-8', 'strict')
    except UnicodeDecodeError as exc:
        assert exc.args[2] == 1

    try:
        b.decode('utf-8', 'replace')
    except UnicodeDecodeError as exc:
        assert exc.args[2] == 1

    try:
        b.decode('utf-8', 'ignore')
    except UnicodeDecodeError as exc:
        assert exc.args[2] == 1

    try:
        b.decode('utf-8', 'backslashreplace')
    except UnicodeDecodeError as exc:
        assert exc.args[2] == 1

    try:
        b.decode('utf-8', 'xmlcharrefreplace')
    except UnicodeDecodeError as exc:
        assert exc.args[2] == 1

    try:
        b.decode
